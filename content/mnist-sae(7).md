Title: MNIST-SAE Log 7
Date: 11/01/2024 23:49
Category: Experiment Logs

## Work Done
- fixed sae shape bug 
- ran visualization code on meta-sae 
- added EMNIST dataset

## Confusions
- how could I measure what changes as you get more meta? 
    - some basic ideas: (LOOK AT THE PAPER!!!)
        - (1) track the amount/trend of nonzero activations
        - (2) track the distribution of nonzero activations (ie are they closer togeter, farther apart etc )
        - (3) track feature descriptions from the eventual auto-interp loop 
- how to deal with large amounts of data (ie downloading these datasets)    
    - how to clean up my mac since it has 300 GB of data somewhere (WHERE?!)

## Next Steps
- fix EMNIST loading (3 dim channel issue again I think?)
- run normal sae on EMNIST
- run meta-sae on EMNIST 
- __Look at the work of the [meta-sae paper](https://www.alignmentforum.org/posts/TMAmHh4DdMr4nCSr5/showing-sae-latents-are-not-atomic-using-meta-saes)__
- (a) make the infinite meta-sae loop (this is probably more fun )
- (b) figure out how to analyze it 
    - VISUALIZE STUFF next time or the time after 
- Transition to ViT at some point

## Cool Stuff
- Google released a new product that allows you to [Learn About](https://learning.google.com/experiments/learn-about) anything deeply with AI