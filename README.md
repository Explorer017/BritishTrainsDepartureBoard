# NationalRailTrainDepartureBoard
![GitHub Repo stars](https://img.shields.io/github/stars/Explorer017/NationalRailTrainDepartureBoard?style=social) ![License](https://img.shields.io/badge/License-MIT-blue) ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/Explorer017/NationalRailTrainDepartureBoard) ![GitHub last commit](https://img.shields.io/github/last-commit/Explorer017/NationalRailTrainDepartureBoard) ![GitHub issues](https://img.shields.io/github/issues-raw/Explorer017/NationalRailTrainDepartureBoard)

A pygame program that immitates the dot matrix departure screens found at National Rail stations, using the [RealTime Trains API](https://api.rtt.io/). 

## Setup

 
 - Sign up for an account on [RealTime Trains](https://api.rtt.io/)
 - Clone the repository, and run the python script:
	  ```
	  $ git clone https://github.com/Explorer017/NationalRailTrainDepartureBoard.git
	  $ python ./main.py
	  ```
- Now, in the newly created `auth.py`, replace `<username>` and `<password` with your RealTime Trains auth credentials

## Usage
Run the Python Script:
```
python ./main.py
```
Then, type in a 3 letter station CRS code (for example: `KGX` for London Kings Cross)
```
Type in a station code: KGX
```
This should open a window with the departure board!

## Licence
See the [LICENCE](https://github.com/Explorer017/NationalRailTrainDepartureBoard/blob/main/LICENCE) file

