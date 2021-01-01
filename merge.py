from argparse import ArgumentParser
import os
import re
def getfile(datapath,etx):
    files = os.listdir(datapath)
    files = list(filter(lambda x:etx in x,files))
    return files
def add_bracket_(filepath):
    fs = open(filepath,'r')
    # print(filepath)
    data = fs.readlines()
    fs.close()
    data = ''.join(data)
    sentences = re.findall('(?<=<s>).+?(?=<\/s>)',data,re.I|re.S)
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
    parser.add_argument('-dp','--data_path',required=True,help='Path to dataset directory, for merge only')
    parser.add_argument('-op','--output_path',required=True,help='Path to output file, file will be created')
    args = parser.parse_args()
    args = vars(args)
    dp = os.path.join(os.getcwd(),args['data_path'])
    op = os.path.join(os.getcwd(),args['output_path'])
    try:
        os.system("rm -rf temp")
        os.system("mkdir -p temp")
        # trick to create file & dirs
        os.system("mkdir -p {}".format(op))
        os.system("rm -rf {}".format(op))
        os.system("touch {}".format(op))

    except OSError:
        print('Some Bug')
    files = getfile(datapath=dp,etx='.prd')
    files = sorted(files)
    for i,file in enumerate(files):
        processed_file_path = add_bracket_(os.path.join(dp,file))
        files[i] = processed_file_path

    with open(op,'w') as f:
        for i,file in enumerate(files):
            fs  = open(file)
            data = fs.readlines()
            fs.close()
            data = ''.join(data)

            f.write(data)
            f.write('\n')

    os.system("rm -rf temp")


