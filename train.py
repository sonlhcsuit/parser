from argparse import ArgumentParser
import os
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-d','--datafile',required=True,help='Path to train data in one file')
    parser.add_argument('-g','--grammar',required=True,help='Path to output grammar file will be created')
    args = parser.parse_args()
    args = vars(args)
    dp = os.path.join(os.getcwd(),args['datafile'])
    op = os.path.join(os.getcwd(),args['grammar'])
    os.system("mkdir -p {}".format(args['grammar']))
    os.system("rm -rf {}".format(args['grammar']))
    os.system("touch {}".format(args['grammar']))

    cmd = "\
    java -cp berkeleyparser/BerkeleyParser-1.7.jar \
    edu.berkeley.nlp.PCFGLA.GrammarTrainer \
    -path {dataset} -out {grammar} \
    -treebank SINGLEFILE".format(dataset=args['datafile'],grammar=args['grammar'])
    print(cmd)
    os.system(cmd)
    # cmd = '\
    # java -cp berkeleyparser/BerkeleyParser-1.7.jar \
    # edu/berkeley/nlp/PCFGLA/WriteGrammarToTextFile \
    # {gr} {gr}.txt'.format(gr=args['grammar'])
    # print(cmd)
    # os.system(cmd)
