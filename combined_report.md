# Combined Markdown Report

## Work Done

### File: mnist-sae(1).md (Date: 10/09/2024 18:40)
### Work Done
- Trained MNIST
- Trained an SAE on MNIST 
- Trained an SAE on an SAE on MNIST 

[__CODE__](https://github.com/jain18ayush/mnist-sae)



### File: mnist-sae(2).md (Date: 10/10/2024 13:20)
### Work Done
- Fixed SAE training + testing code 
- Analyzed max activations of mnist, sae, and meta-sae 

[__CODE__](https://github.com/jain18ayush/mnist-sae)



### File: mnist-sae(3).md (Date: 10/11/2024 17:49)
### Work Done
- analyzed MNIST through generating maximally activating images for each neuron in layer fc2
- looked at SAE reconstructions + maximal activations for SAE and Meta-SAE 
    - also looked at cosine similarity between them 
    - and max activating features 
    - also made a 2d PCA 

[__CODE__](https://github.com/jain18ayush/mnist-sae)



### File: vit-sae(1).md (Date: 10/15/2024 16:11)
### Work Done
- Wrote some boilerplate Vit and training it currently (it is based off of a google one so may not have 'pure?' results ). I guess purity in this sense is just wondering about the dataset used to train teh other. Though it should not matter on a representation level since dataset has a set of images.But if there are completely different images we will not be able to capture it. 
- installed vit-prisma and attempted to use its vit training code
- gave up on MNIST sae since could not figure out how to parse the features --> lack of data (just 9 categories) 

[__Code__](https://colab.research.google.com/drive/17UrjkTMIrfSJJB7l-I0MS4AgnXvKDX1a#scrollTo=mkN4po99_bjk)



### File: vit-sae(2).md (Date: 10/20/2024 23:43)
### Work Done
- created some basic training code for a vit --> might take forever to run



### File: vit-sae(3).md (Date: 10/21/2024 21:19)
### Work Done
- loaded in the dsprites dataset + got it preprocessed properly 
- created the probes 
- refactored a bit of the dataset and model structs



### File: vit-sae(4).md (Date: 10/22/2024 23:18)
### Work Done
- Loaded in data by label for the dsprites data 
- attempted to start linear probe training 
- looked at [refactoring + design pattern](https://www.perplexity.ai/search/what-are-some-good-channels-li-dyJf2sSIQa6ydXemcGxAbQ) stuff



### File: mnist-sae(4).md (Date: 10/29/2024 11:12)
### Work Done
- Loaded in CIFAR-10 data
- ran it through MNIST + the first sae
- cached all the activations 
- found max activating images



### File: mnist-sae(5).md (Date: 10/30/2024 11:35)
### Work Done
- found a bug in the caching code that resulted in incorrect caching (ie getting 150k samples as opposed to 50k inputted)



### File: mnist-sae(6).md (Date: 10/31/2024 16:55)
### Work Done
- cleaned up training pipeline for mnist saes 
- fixed dimension error where I was passing in the wrong channle (3 channel as opposed to 1) and fixed it so the MNIST was 3 channel input 
    - standardization of images 
- added caching code to the EnhancedSAE since it seems to perform better
- attempted to visualize meta-sae but ran into a bug



### File: mnist-sae(7).md (Date: 11/01/2024 23:49)
### Work Done
- fixed sae shape bug 
- ran visualization code on meta-sae 
- added EMNIST dataset



### File: mnist-sae(8).md (Date: 11/03/2024 00:32)
### Work Done
- Loaded in EMNIST dataset and ran an SAE + meta-sae on it.



### File: mnist-sae(9).md (Date: 11/03/2024 20:44)
### Work Done
- set up initial loop for infinite saes



### File: mnist-sae(10).md (Date: 11/04/2024 23:31)
### Work Done
- set up loop for generating images for all the depths 
- started looking into the [Meta-SAE Paper](https://www.alignmentforum.org/posts/TMAmHh4DdMr4nCSr5/showing-sae-latents-are-not-atomic-using-meta-saes). This is the [chatgpt partial explanation](https://chatgpt.com/c/6729ad14-4880-8004-acfc-60a3f2d43514)



### File: mnist-sae(11).md (Date: 11/09/2024 23:56)
### Work Done
- Established rudimentary interp via EMNIST classification labels 
- Fixed up some of the experiment code to sagve the indices 
- got preliminary findings that there is a optimal depth for meta-saes

- Found that the average amount of activations do increase the deeper you go which implies some level of fine-grained-ness 
- The amount of activaitons of the max hit their peak at 2 depths in.




---

## Confusions

### File: mnist-sae(1).md (Date: 10/09/2024 18:40)
### Confusions
- Why does the SAE have a smaller hidden dim rather than a larger one? 
- What does success look like for this project 
- How would I track which neurons are [curve detectors](https://distill.pub/2020/circuits/curve-detectors/)?



### File: mnist-sae(2).md (Date: 10/10/2024 13:20)
### Confusions
- What else can I do besides max activations to track features + latents?
- What happens when I do the decoder instead of the encoder? Can I take something out of the decoder or is the activation just the output.



### File: mnist-sae(3).md (Date: 10/11/2024 17:49)
### Confusions
- What do the maximally activating images mean? 
- What do the cosine sims + PCA mean 
- Should I switch to doing this on gpt2 or a transformer model (maybeAudioLM](https://google-research.github.io/seanet/audiolm/examples/) or [whisper](https://er537.github.io/blog/2023/09/05/whisper_interpretability.html))
- ***How does any of this relate to features?*** 
- Does improving the optimization algorithm significantly change the optimized images generated (does it parse the internals meaningfully better)



### File: vit-sae(1).md (Date: 10/15/2024 16:11)
### Confusions
- How do they eval
- Which layer is good
- Do i Need better saes
- Will I run into the same data issue with these SAEs ?



### File: vit-sae(2).md (Date: 10/20/2024 23:43)
### Confusions
- what can I measure in devinterp 
    - vit seems nice because I can train it pretty easily as opposed to gpt-2



### File: vit-sae(3).md (Date: 10/21/2024 21:19)
### Confusions
- What is a linear probe? Like actually. 
- what is a good way to manage storage?



### File: vit-sae(4).md (Date: 10/22/2024 23:18)
### Confusions
- should I train on mlp or logistic regression? 
    - does it matter?



### File: mnist-sae(4).md (Date: 10/29/2024 11:12)
### Confusions
- struggling to understand does the dataset have a constat image that it pulls from or is it randomized every time? 
    - need to validate that the images are not random or that I can control them 
- how do I actually visualize the clean image from CIFAR-10?



### File: mnist-sae(5).md (Date: 10/30/2024 11:35)
### Confusions
- why is the bug happening



### File: mnist-sae(6).md (Date: 10/31/2024 16:55)
### Confusions
- How is a model like an autoencoder capable of learning? Like what mathematically allows for it?



### File: mnist-sae(7).md (Date: 11/01/2024 23:49)
### Confusions
- how could I measure what changes as you get more meta? 
    - some basic ideas: (LOOK AT THE PAPER!!!)
        - (1) track the amount/trend of nonzero activations
        - (2) track the distribution of nonzero activations (ie are they closer togeter, farther apart etc )
        - (3) track feature descriptions from the eventual auto-interp loop 
- how to deal with large amounts of data (ie downloading these datasets)    
    - how to clean up my mac since it has 300 GB of data somewhere (WHERE?!)



### File: mnist-sae(8).md (Date: 11/03/2024 00:32)
### Confusions
- how do I measure the impact of continuous meta-saes? 
    - run MNIST dataset and see if there are more distinct pattenrs that emerge over time



### File: mnist-sae(9).md (Date: 11/03/2024 20:44)
### Confusions
- analysis how? 
- should I pivot to ... EMNIST? or another mnist dataset



### File: mnist-sae(10).md (Date: 11/04/2024 23:31)
### Confusions
- what is a meta-sae latent
- what is an sae latent

- Why do the activation trends decrease over time.



### File: mnist-sae(11).md (Date: 11/09/2024 23:56)
### Confusions
- Am I actually doing what I think I am doing? 
    - what I am trying to do: Take a trained MNIST model, feed it MNIST data, train an SAE on those. Track the values with EMNIST data to see what patterns there are outside of numbers ( in this case a balanced dataset of letters and numbers)
    - the max activatoins are seeing if tehre are any neurons taht fire exclusively on one label OR if there are some basic trends like letters and numbers




---

## Next Steps

### File: mnist-sae(1).md (Date: 10/09/2024 18:40)
### Next Steps
- Track the max activations of 
    - MNIST neurons
    - SAE1 neurons 
    - SAE2 neurons 
- See whether the activations become more concentrated as you go down. So the idea is that on mnist the neurons activate strongly on 3 numbers, on the sae1 it will be on 2 numbers and on sae2 it may be on 1 numbe really strongly. 
    - This would imply that the features become more atomic as you go down 

*Stream Link:* [*https://youtube.com/live/QG-YNsHa0EQ*](https://youtube.com/live/QG-YNsHa0EQ)



### File: mnist-sae(2).md (Date: 10/10/2024 13:20)
### Next Steps
- Analyze the activations to look for 
    - Which predictions had the most activations 
    - What was the spread of predictions for each neuron
    - Track the sparsity count 
- **Look at [showing-sae-latents-are-not-atomic-using-meta-saes](https://www.alignmentforum.org/posts/TMAmHh4DdMr4nCSr5/showing-sae-latents-are-not-atomic-using-meta-saes) to see how they analyzed meta saes** 

*Stream Link:* [*https://youtube.com/live/vBzGeV1ZaTQ*](https://youtube.com/live/vBzGeV1ZaTQ)



### File: mnist-sae(3).md (Date: 10/11/2024 17:49)
### Next Steps
- Find out how to save everything to a pdf as reports 
- Analyze it? for... seeing what each neuron in the SAE represents 
-   But how did they run max activaitons through the meta-sae?? they as in: - **[showing-sae-latents-are-not-atomic-using-meta-saes](https://www.alignmentforum.org/posts/TMAmHh4DdMr4nCSr5 showing-sae-latents-are-not-atomic-using-meta-saes)** 
- Generate thea ctivation map for fc1 on MNIST



### File: vit-sae(1).md (Date: 10/15/2024 16:11)
### Next Steps
- Read [State of Vision Interp](https://www.soniajoseph.ai/multimodal-interpretability-in-2024/) + other background resources 
- Train a ViT
    - [Smaller Raw One](https://github.com/sheikheddy/PyTorch-Scratch-Vision-Transformer-ViT)
- Train an SAE on the Vit
- Follow others in evaluating the SAE 
    - [ViT-Prisma Evals](https://github.com/soniajoseph/ViT-Prisma/blob/main/demos/Train_CLIP_SAE.ipynb)
    - [Hugo Fry's ViT Sae](https://github.com/soniajoseph/ViT-Prisma/blob/main/demos/Train_CLIP_SAE.ipynb)



### File: vit-sae(2).md (Date: 10/20/2024 23:43)
### Next Steps
- create a vit trained on cifar-10 or pokemon cards 
    - use [Prisma Training Code](https://github.com/soniajoseph/ViT-Prisma/blob/main/docs/UsageGuide.md)
- analyze at what point it can recognize a circle vs a square 
    - use the [shapes dataset](https://github.com/google-deepmind/dsprites-dataset) from vit



### File: vit-sae(3).md (Date: 10/21/2024 21:19)
### Next Steps
- Need to make the full data pipeline. dsprites data --> embedding extraction from every layer --> train a linear probe --> validate accuracy 
- Make some graphs next time



### File: mnist-sae(4).md (Date: 10/29/2024 11:12)
### Next Steps
- Visualize the images [x]
- Visualize the images with [ImageNet](https://paperswithcode.com/dataset/imagenet) or another image set that has way more diverse images 
- Repeat the process for the meta-sae 
- utilize VLM to do labeling (maybe CLIP?)
- go really meta and have a loop that continously constructs meta-saes 
        - trying to find if there is a point at which you cannot get more fine-grained



### File: mnist-sae(5).md (Date: 10/30/2024 11:35)
### Next Steps
- fix the bug



### File: mnist-sae(6).md (Date: 10/31/2024 16:55)
### Next Steps
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



### File: mnist-sae(7).md (Date: 11/01/2024 23:49)
### Next Steps
- fix EMNIST loading (3 dim channel issue again I think?)
- run normal sae on EMNIST
- run meta-sae on EMNIST 
- __Look at the work of the [meta-sae paper](https://www.alignmentforum.org/posts/TMAmHh4DdMr4nCSr5/showing-sae-latents-are-not-atomic-using-meta-saes)__
- (a) make the infinite meta-sae loop (this is probably more fun )
- (b) figure out how to analyze it 
    - VISUALIZE STUFF next time or the time after 
- Transition to ViT at some point



### File: mnist-sae(8).md (Date: 11/03/2024 00:32)
### Next Steps
- Graph the activation distribution for the sae vs the meta-sae 
    - this claude chat has some of the [code](https://claude.ai/chat/925ecbb6-227c-4d90-8f35-609ba2d310dc)
- __Look at the work of the [meta-sae paper](https://www.alignmentforum.org/posts/TMAmHh4DdMr4nCSr5/showing-sae-latents-are-not-atomic-using-meta-saes)__
    - distill it down into notes and replicate its experiments 
- Deploy the site at some point



### File: mnist-sae(9).md (Date: 11/03/2024 20:44)
### Next Steps
- DO 1 epoch for testing purposes

- look into the normalization values for the transforms of emnist and mnist 
- finish that loop
- clear out activations 
- analyze the activations
- think about latents



### File: mnist-sae(10).md (Date: 11/04/2024 23:31)
### Next Steps
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



### File: mnist-sae(11).md (Date: 11/09/2024 23:56)
### Next Steps
- Plot some of the data using the [techniques from GPT](https://chatgpt.com/c/67305526-3b20-8004-bcc0-1d870e8904d0)
- __Create a preliminary writeup using the charts and any other ones to show what i have so far__ 
    - REPLICATE, REPLICATE, REPLICATE with other datasets (like fruit or other EMNISTs) --> basically take all the classification datasets 
- Also need to look at the analysis for the [meta-sae paper](https://www.alignmentforum.org/posts/TMAmHh4DdMr4nCSr5/showing-sae-latents-are-not-atomic-using-meta-saes)




---

## Cool Stuff

### File: mnist-sae(5).md (Date: 10/30/2024 11:35)
### Cool Stuff
[VLM - openbmb/MiniCPM-V-2](https://huggingface.co/openbmb/MiniCPM-V-2)
[Pytorch Datasets](https://pytorch.org/vision/stable/datasets.html)




---

