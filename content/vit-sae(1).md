Title: ViT-SAE Log 1
Date: 10/15/2024 16:11
Category: Experiment Logs

## Background
Attempting to create Meta-SAEs on a classification Vit. The hope is that this gives more access to fine-grained features. 

[Meta-SAE](https://www.alignmentforum.org/posts/TMAmHh4DdMr4nCSr5/showing-sae-latents-are-not-atomic-using-meta-saes)
[ViT-SAE Training](https://www.lesswrong.com/posts/bCtbuWraqYTDtuARg/towards-multimodal-interpretability-learning-sparse-2)

[State of Vision Interp](https://www.soniajoseph.ai/multimodal-interpretability-in-2024/)
## Work Done
- Wrote some boilerplate Vit and training it currently (it is based off of a google one so may not have 'pure?' results ). I guess purity in this sense is just wondering about the dataset used to train teh other. Though it should not matter on a representation level since dataset has a set of images.But if there are completely different images we will not be able to capture it. 
- installed vit-prisma and attempted to use its vit training code
- gave up on MNIST sae since could not figure out how to parse the features --> lack of data (just 9 categories) 

[__Code__](https://colab.research.google.com/drive/17UrjkTMIrfSJJB7l-I0MS4AgnXvKDX1a#scrollTo=mkN4po99_bjk)

## Confusions
- How do they eval
- Which layer is good
- Do i Need better saes
- Will I run into the same data issue with these SAEs ? 

## Next Steps
- Read [State of Vision Interp](https://www.soniajoseph.ai/multimodal-interpretability-in-2024/) + other background resources 
- Train a ViT
    - [Smaller Raw One](https://github.com/sheikheddy/PyTorch-Scratch-Vision-Transformer-ViT)
- Train an SAE on the Vit
- Follow others in evaluating the SAE 
    - [ViT-Prisma Evals](https://github.com/soniajoseph/ViT-Prisma/blob/main/demos/Train_CLIP_SAE.ipynb)
    - [Hugo Fry's ViT Sae](https://github.com/soniajoseph/ViT-Prisma/blob/main/demos/Train_CLIP_SAE.ipynb)

## GOAL: Reproduce the Vit Prisma SAE training and then run a Meta-SAE on it. 