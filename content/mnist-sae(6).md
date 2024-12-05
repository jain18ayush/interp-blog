Title: MNIST-SAE Log 6
Date: 10/31/2024 16:55
Category: Experiment Logs

## Work Done
- cleaned up training pipeline for mnist saes 
- fixed dimension error where I was passing in the wrong channle (3 channel as opposed to 1) and fixed it so the MNIST was 3 channel input 
    - standardization of images 
- added caching code to the EnhancedSAE since it seems to perform better
- attempted to visualize meta-sae but ran into a bug 

## Confusions
- How is a model like an autoencoder capable of learning? Like what mathematically allows for it? 

## Next Steps
- figure out shape error bug (this is like 90% of the bugs I face) [x]
- run the image visualization on the meta-sae [x]
- fully establish the experiment pipelin to actually test whether the meta-sae has different representations
    - (1) track the amount of 10+ image pairs 
        - as a future step make it unbounded rather than picking only top 10 or play with thresholds 
    - (2) set up a VLM do to auto-interp
        - open source it? 
        - Ask Louka (from slack) how he did interp for his vision sae 
- Once I have a working analysis portion set up infinite sae training
    - need a bigger dataset and/or (probably a train test split weighted 80% towards test side for MNIST) 
- Look at [Top-K Sae](https://cdn.openai.com/papers/sparse-autoencoders.pdf) and maybe use it since current training trends are pretty bad (>= 7.0 loss)
