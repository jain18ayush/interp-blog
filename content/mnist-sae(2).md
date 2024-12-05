Title: MNIST-SAE Log 2
Date: 10/10/2024 13:20
Category: Experiment Logs

## Work Done
- Fixed SAE training + testing code 
- Analyzed max activations of mnist, sae, and meta-sae 

[__CODE__](https://github.com/jain18ayush/mnist-sae)

## Confusions
- What else can I do besides max activations to track features + latents?
- What happens when I do the decoder instead of the encoder? Can I take something out of the decoder or is the activation just the output. 

## Observations 
- The sae features become more sparse as you do more SAEs 
- The activation values become really small as well <1
- the meta-sae had neuron 4 activate a lot 

## Next Steps 
- Analyze the activations to look for 
    - Which predictions had the most activations 
    - What was the spread of predictions for each neuron
    - Track the sparsity count 
- **Look at [showing-sae-latents-are-not-atomic-using-meta-saes](https://www.alignmentforum.org/posts/TMAmHh4DdMr4nCSr5/showing-sae-latents-are-not-atomic-using-meta-saes) to see how they analyzed meta saes** 

*Stream Link:* [*https://youtube.com/live/vBzGeV1ZaTQ*](https://youtube.com/live/vBzGeV1ZaTQ)
