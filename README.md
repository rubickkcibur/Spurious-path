# Path Spuriousness-aware Reinforcement Learning for Multi-hop Knowledge Graph Reasoning

Our implementation is based on official codes of [MultiHop](https://github.com/salesforce/MultiHopKG). Best regards to their contribution.

## Quick Start

#### Mannually set up 
```
conda install --yes --file requirements.txt
```

### Process data
You can fetch `umls`, `kinship`, `wn18rr`, `nell-995` from [MultiHop](https://github.com/salesforce/MultiHopKG).

Then run the following command to preprocess the datasets.
```
./experiment.sh configs/<dataset>.sh --process_data <gpu-ID>
```

`<dataset>` is the name of any dataset folder in the `./data` directory.

### Train models
Then the following commands can be used to train the proposed models and baselines in the paper. By default, dev set evaluation results will be printed when training terminates.

1. Train embedding-based models
```
./experiment-emb.sh configs/<dataset>-<emb_model>.sh --train <gpu-ID>
```
The following embedding-based models are implemented: `distmult`, `complex` and `conve`.

2. Train RL models (policy gradient)
```
./experiment.sh configs/<dataset>.sh --train <gpu-ID>
```

3. Train RL models (policy gradient + reward shaping)
```
./experiment-rs.sh configs/<dataset>-rs.sh --train <gpu-ID>
```

4. Train PS-aware RL models
```
./experiment-rs.sh configs/<dataset>-conf.sh --train <gpu-ID>
```

* Note: To train the RL models using reward shaping, make sure 1) you have pre-trained the embedding-based models and 2) set the file path pointers to the pre-trained embedding-based models correctly ([example configuration file](configs/umls-rs.sh)).

### Evaluate pretrained models
To generate the evaluation results of a pre-trained model, simply change the `--train` flag in the commands above to `--inference`. 

For example, the following command performs inference with the RL models (policy gradient + reward shaping) and prints the evaluation results (on both dev and test sets).
```
./experiment-rs.sh configs/<dataset>-conf.sh --inference <gpu-ID>
```

To have evaluation on PS metric, use the `--save_beam_search_paths` flag:
```
./experiment-rs.sh configs/<dataset>-conf.sh --inference <gpu-ID> --save_beam_search_paths
```

* Note: `--save_beam_search_paths` flag is not applicable for embedding models for they have no reasoning paths 

* Note for the NELL-995 dataset: 

  On this dataset we split the original training data into `train.triples` and `dev.triples`, and the final model to test has to be trained with these two files combined. 
  1. To obtain the correct test set results, you need to add the `--test` flag to all data pre-processing, training and inference commands.  
    ```
    # You may need to adjust the number of training epochs based on the dev set development.

    ./experiment.sh configs/nell-995.sh --process_data <gpu-ID> --test
    ./experiment-emb.sh configs/nell-995-conve.sh --train <gpu-ID> --test
    ./experiment-rs.sh configs/NELL-995-conf.sh --train <gpu-ID> --test
    ./experiment-rs.sh configs/NELL-995-conf.sh --inference <gpu-ID> --test
    ```    
  2. Leave out the `--test` flag during development.

### Change the hyperparameters
To change the hyperparameters and other experiment set up, start from the [configuration files](configs).
