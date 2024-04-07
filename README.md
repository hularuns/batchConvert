# GIS Batch Converter Tool

A tool which will batch convert files from a range GIS file formats and conversions between common CRS.

## Getting Started


### Prerequisites

Python 3 will need to be installed prior to installation.

If you choose not to use `pip` conda will need to be installed.

The installation will involve installing a conda environment which makes use of geopandas.


### Installing
#### Pip install
Install geopandas using `pip install geopandas`.

#### Conda Environment

You can also create a conda environment using Python 3 and above using the [environment.yml](environment.yml). 

Open the acaconda prompt and navigate to the project folder, e.g. *C:/Users/(username)/projects/batchConvert*.

Then type the following into the prompt to create a conda environment for the batch convert tool.

```
conda env create --file=environment.yml

conda activate batchConvert
```

Once the environment has been activated, in your anaconda prompt you should see:
`(batchConvert) C:\Users\(username)\projects\batchConvert`

To run the batch convert tool, type the following within the anaconda prompt with the batchConvert environment activated.

```
python batchConvert.py
```


## Running the tool

Instructions on how to input and expect outputs to look like to be added at a later date once further along development.


## Built With

* [Python 3.12](https://www.python.org/) 


## Authors

* **Sam Groves** - *Ecologist and student* - [Sam Groves](https://github.com/hularuns)

## 

## License

This project is licensed under the GNU (v3) License - see the file [LICENSE.md](LICENSE) for details.

## Acknowledgments

* Hat tip to anyone whose code was used (stackexchange, looking at you!)
* Inspiration
* etc

