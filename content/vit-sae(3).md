Title: ViT-SAE Log 3
Date: 10/21/2024 21:19
Category: Experiment Logs

## Work Done
- loaded in the dsprites dataset + got it preprocessed properly 
- created the probes 
- refactored a bit of the dataset and model structs

## Confusions
- What is a linear probe? Like actually. 
- what is a good way to manage storage? 

## Next Steps
- Need to make the full data pipeline. dsprites data --> embedding extraction from every layer --> train a linear probe --> validate accuracy 
- Make some graphs next time 

## Cool Stuff
- List of all datasets in pytorch: [https://pytorch.org/vision/stable/datasets.html](https://pytorch.org/vision/stable/datasets.html)
- [hdf5 file format](https://docs.h5py.org/en/stable/) for hierarchical storage 
- [Discussion of Pythia as a model for devinterp research](https://x.com/dpaleka/status/1848378815573065935)