Title: MNIST-SAE Log 10
Date: 11/04/2024 23:31
Category: Experiment Logs

## Work Done
- set up loop for generating images for all the depths 
- started looking into the [Meta-SAE Paper](https://www.alignmentforum.org/posts/TMAmHh4DdMr4nCSr5/showing-sae-latents-are-not-atomic-using-meta-saes). This is the [chatgpt partial explanation](https://chatgpt.com/c/6729ad14-4880-8004-acfc-60a3f2d43514)

## Confusions
- what is a meta-sae latent
- what is an sae latent

- Why do the activation trends decrease over time. 

## Next Steps
- WRITE UP A Document compiled what I have found --> communicate it well. Does not matter if it means nothing just have it out there. 
    - (1) Look over every log I ever wrote and compile the next steps learnings questions etc.
        - Can also write a script to do it but it probably takes away from the reflection component. 
    - (2) Try to answer some of the questions 
    - (3) Create graphs to show data and pick out interesting ones 
- Post that document here? Maybe on lesswrong. 

- train meta-saes on different dictionary sizes (maybe double the deeper you go)
- auto-interp : pretty useful for EMNIST or MNIST since it could just find the ones. 
    - alternatively we can use our EMNIST classifier to take the images and get the predictions on each one. 
        - [__WavMix is the SOTA Classifier for EMNIST__](https://github.com/pranavphoenix/WaveMix)
    - Can use a different dataset since we have CIFAR100 but those are categories so not as fine-tuned? Probably good enough though. 
        - [SAM by Google is the SOTA for CIFAR100](https://github.com/google-research/sam)
    - if there is a neuron that maximizes on a specific class then that could be interesting 
    - __Might have to regenerate the images to be easier to split or have them generated separately into folders?__
    - [Hugo Fry's Github](https://github.com/HugoFry/mats_sae_training_for_ViTs/blob/main/vit_sae_analysis/dashboard_fns.py) has feature activation analysis stuff which could be useful if I ask gpt/claude about how to use it for my code 

