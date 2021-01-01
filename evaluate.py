from argparse import ArgumentParser
import os
import re
def getfile(datapath,etx):
    files = os.listdir(datapath)
    files = list(filter(lambda x:etx in x,files))
    return files
def add_bracket_(filepath):
    fs = open(filepath,'r')
    print(filepath)
    data = fs.readlines()
    fs.close()
    data = ''.join(data)

    out = []
    for sentence in sentences:
        out.append("({})".format(sentence.strip()))

    temp_path = os.path.join(os.getcwd(),'temp',"{}.temp".format(filepath.split('/')[-1]))
    fs = open(temp_path,'w')
    fs.write('\n'.join(out))
    fs.close()
    return temp_path

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-td','--test_path',required=True,help='Path to test directory')
    parser.add_argument('-g','--grammar',required=True,help='Path to output grammar file (model)')
    parser.add_argument('-r','--result',required=True,help='Path to result directory, will be created')

    args = parser.parse_args()
    args = vars(args)
    tp = os.path.join(os.getcwd(),args['test_path'])
    gp = os.path.join(os.getcwd(),args['grammar'])
    rp = os.path.join(os.getcwd(),args['result'])

    # Select all .prd file
    goals = getfile(tp,'.prd')
    goals = sorted(goals)
    # Create files
    os.system('mkdir -p {}'.format(os.path.join(rp,'raw.mrg')))
    os.system('rm -rf {}/'.format(os.path.join(rp,'raw.mrg')))
    os.system('mkdir -p {}'.format(os.path.join(rp, 'goal.mrg')))
    os.system('rm -rf {}/'.format(os.path.join(rp, 'goal.mrg')))

    fs1 = open(os.path.join(rp,'raw.mrg'),'w')
    fs2 = open(os.path.join(rp,'goal.mrg'),'w')

    for goal in goals:
        # print(goal)
        fs = open(os.path.join(tp,goal),'r')
        lines = fs.readlines()
        lines = ''.join(lines)
        trees = re.findall('(?<=<s>).+?(?=<\/s>)', lines, re.I | re.S)
        for tree in trees:
            words = re.findall('(?<=\()[^\(]*?(?=\))',tree,re.I|re.S)
            sentences = []
            for word in words:
                label,ct = word.split(' ')
                if label != 'NONE' and '*' not in ct:
                    sentences.append(ct.replace('_',' '))
            sentence = ' '.join(sentences)
            fs1.write(sentence)
            fs1.write('\n')
            tree = tree.replace('\n','')
            tree = re.sub('\s+',' ',tree.replace('\n',' '))
            print(tree)
            fs2.write('( {} )'.format(tree))
            fs2.write('\n')
            # break
        # break
    fs1.close()
    fs2.close()
    # Evaluate
    cmd = 'java -jar berkeleyparser/BerkeleyParser-1.7.jar \
    -gr {} < {} >> {}'.format(gp,rp+'/raw.mrg',os.path.join(rp,'predicted.mrg'))
    print(cmd)
    # os.system(cmd)
    print('Predict Done')