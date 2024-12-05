Title: MNIST-SAE Log 4
Date: 10/29/2024 11:12
Category: Experiment Logs

## Work Done
- Loaded in CIFAR-10 data
- ran it through MNIST + the first sae
- cached all the activations 
- found max activating images
## Confusions
- struggling to understand does the dataset havfe a constat image that it pulls from or is it randomized every time? 
    - need to validate that the images are not random or that I can control them 
- how do I actually visualize the clean image from CIFAR-10?

## Next Steps
- Visualize the images [x]
- Visualize the images with [ImageNet](https://paperswithcode.com/dataset/imagenet) or another image set that has way more diverse images 
- Repeat the process for the meta-sae 
- utilize VLM to do labeling (maybe CLIP?)
- go really meta and have a loop that continously constructs meta-saes 
        - trying to find if there is a point at which you cannot get more fine-grained

## Cool Stuff
- [Hugo Fry's experiments with Vision SAEs](https://www.lesswrong.com/posts/bCtbuWraqYTDtuARg/towards-multimodal-interpretability-learning-sparse-2)
- [Hugo Fry et al. work with medical saes](https://www.lesswrong.com/posts/3FcXL2NYJaBdGWrCW/an-x-ray-is-worth-15-features-sparse-autoencoders-for) : Ranjani could be interested in this 