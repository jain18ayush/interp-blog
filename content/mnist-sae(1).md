Title: MNIST-SAE Log 1 
Date: 10/09/2024 18:40
Category: Experiment Logs 

## Background
Sparse Autoencoders are a way to understand the internal structure of model computations. The principle is that you take the activations of a model, train an SAE on it and then do max activation tracking to see what neurons in the sae fire the most on some set of concepts. This works is an attempt to extend/replicate the paper [Showing SAE Latents Are Not Atomic Using Meta-SAEs](https://www.alignmentforum.org/posts/TMAmHh4DdMr4nCSr5/showing-sae-latents-are-not-atomic-using-meta-saes) which trained SAEs on an SAE that was trained on gpt-2 small residual stream. The goal of my work is train an SAE on an SAE trained on MNIST. I am still trying to figure out what will happen (maybe there will be max activations that activate on more *curvy* numbers). 

## Work Done
- Trained MNIST
- Trained an SAE on MNIST 
- Trained an SAE on an SAE on MNIST 

[__CODE__](https://github.com/jain18ayush/mnist-sae)

## Confusions
- Why does the SAE have a smaller hidden dim rather than a larger one? 
- What does success look like for this project 
- How would I track which neurons are [curve detectors](https://distill.pub/2020/circuits/curve-detectors/)?

## Next Steps 
- Track the max activations of 
    - MNIST neurons
    - SAE1 neurons 
    - SAE2 neurons 
- See whether the activations become more concentrated as you go down. So the idea is that on mnist the neurons activate strongly on 3 numbers, on the sae1 it will be on 2 numbers and on sae2 it may be on 1 numbe really strongly. 
    - This would imply that the features become more atomic as you go down 

*Stream Link:* [*https://youtube.com/live/QG-YNsHa0EQ*](https://youtube.com/live/QG-YNsHa0EQ)
