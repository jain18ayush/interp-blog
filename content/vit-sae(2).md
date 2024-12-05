Title: ViT-SAE Log 2
Date: 10/20/2024 23:43
Category: Experiment Logs

## Background
[Devinterp](https://github.com/timaeus-research/devinterp) is the field that seeks to understand what leads to the emergence of model properties during training. I think it would be cool to use linear probes to examine when and where meaningful features emerge in a model. 
## Work Done
- created some basic training code for a vit --> might take forever to run 
## Confusions
- what can I measure in devinterp 
    - vit seems nice because I can train it pretty easily as opposed to gpt-2
## Next Steps
- create a vit trained on cifar-10 or pokemon cards 
    - use [Prisma Training Code](https://github.com/soniajoseph/ViT-Prisma/blob/main/docs/UsageGuide.md)
- analyze at what point it can recognize a circle vs a square 
    - use the [shapes dataset](https://github.com/google-deepmind/dsprites-dataset) from vit 

## GOAL: Reproduce the Vit Prisma SAE training and then run a Meta-SAE on it OR run dev interp experiments to analyze at what point does a certain feature emerge
