Title: MNIST-SAE Log 11
Date: 11/09/2024 23:56
Category: Experiment Logs

## Work Done
- Established rudimentary interp via EMNIST classification labels 
- Fixed up some of the experiment code to sagve the indices 
- got preliminary findings that there is a optimal depth for meta-saes

- Found that the average amount of activations do increase the deeper you go which implies some level of fine-grained-ness 
- The amount of activaitons of the max hit their peak at 2 depths in. 

## Confusions
- Am I actually doing what I think I am doing? 
    - what I am trying to do: Take a trained MNIST model, feed it MNIST data, train an SAE on those. Track the values with EMNIST data to see what patterns there are outside of numbers ( in this case a balanced dataset of letters and numbers)
    - the max activatoins are seeing if tehre are any neurons taht fire exclusively on one label OR if there are some basic trends like letters and numbers 

## Next Steps
- Plot some of the data using the [techniques from GPT](https://chatgpt.com/c/67305526-3b20-8004-bcc0-1d870e8904d0)
- __Create a preliminary writeup using the charts and any other ones to show what i have so far__ 
    - REPLICATE, REPLICATE, REPLICATE with other datasets (like fruit or other EMNISTs) --> basically take all the classification datasets 
- Also need to look at the analysis for the [meta-sae paper](https://www.alignmentforum.org/posts/TMAmHh4DdMr4nCSr5/showing-sae-latents-are-not-atomic-using-meta-saes)

## Cool Stuff
- [Fruit Classification Dataset](https://www.kaggle.com/code/dipuk0506/spinalnet-fruit360-99-99-accuracy): Has 141 Classes
- [SAE Vision Explainability](https://arxiv.org/abs/2406.03662)
- [Transcoders](https://arxiv.org/pdf/2406.11944) as a way to interpret MLP layers