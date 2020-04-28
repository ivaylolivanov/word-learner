# Word learner

## Description
	The goal of the script is to help its users learn quicker new words in
	a given language.
	The user selects the language to translate to. The word list
	is created and maintained by the user. At the end of the
	execution, the script shows the correct and the incorrect
	translations.

## Requirements
	The script assumes only the presence of python3

## Usage
    Execution of the script:
	<SCRIPT> <Language to translate to> <Path to json file>
	The json word list follows the following pattern:
	{
		...,
		"Word" : {
			"Language" : "Language of the word",
			"Translations" : {
				"Language1" : [List of translations in language1],
				"Language2" : [List of translations in language1],
				...
			}
		},
		...
	}
