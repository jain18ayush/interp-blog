Title: MNIST-SAE Log 3
Date: 10/11/2024 17:49
Category: Experiment Logs

### Goal: Figure out what features (as in curves, numbers, thoughts, ideas) are inside MNIST. Want to break it apart akin to breaking apart a transformer with an SAE (visualizations and stuff)

## Work Done
- analyzed MNIST through generating maximally activating images for each neuron in layer fc2
- looked at SAE reconstructions + maximal activations for SAE and Meta-SAE 
    - also looked at cosine similarity between them 
    - and max activating features 
    - also made a 2d PCA 

[__CODE__](https://github.com/jain18ayush/mnist-sae)

## Confusions
- What do the maximally activating images mean? 
- What do the cosine sims + PCA mean 
- Should I switch to doing this on gpt2 or a transformer model (maybeAudioLM](https://google-research.github.io/seanet/audiolm/examples/) or [whisper](https://er537.github.io/blog/2023/09/05/whisper_interpretability.html))
- ***How does any of this relate to features?*** 
- Does improving the optimization algorithm significantly change the optimized images generated (does it parse the internals meaningfully better)

## Observations 
- The 2d Latent space of SAE has a right Angle. Appears there are two directions. 
- The cosine similarity is far more sparse on the Meta-SAE than the SAE 
- There is only one direction in the latent space of the MEta-SAE
- There are two distinct types of noise images in the pictures === The first is like a barcode while the others are a gray fuzzy mess

## Next Steps 
- Find out how to save everything to a pdf as reports 
- Analyze it? for... seeing what each neuron in the SAE represents 
-   But how did they run max activaitons through the meta-sae?? they as in: - **[showing-sae-latents-are-not-atomic-using-meta-saes](https://www.alignmentforum.org/posts/TMAmHh4DdMr4nCSr5 showing-sae-latents-are-not-atomic-using-meta-saes)** 
- Generate thea ctivation map for fc1 on MNIST 

## Big Question: How do I look at a neuron in an SAE and tell what feature of the larger model it is representing?

*Stream Link:* [*https://youtube.com/live/pX6yByN8AFo*](https://youtube.com/live/pX6yByN8AFo)
