## CLI
- use this command to merge all treebank into one file & change format.
```shell script
python3 merge.py -dp sample/ -op merged_sample.mrg
```
- use this command to train 
- all grammars will be saved in to grs dir
```shell script
python3 train.py -d merged_sample.mrg -g grs/
```