# json-text-game
A simplified python script to parse a JSON file to play a generalized choose your own adventure text game. 

The goals of this project are the following: 
- Flexible and easy to configure JSON file. 
- Support for multiple story styles, such as linear, looping, and branching. 
- No need for average use case to require code modification. 

## Game JSON Format  

### Example format: 
```json
{
	"game": {
        "0":{
			"textbody": "I am what will be displayed on screen to the user. I'm best for the story, such as 'you wander to the mouth of a forest...' ",
			"optionbody": "I am best for displaying options, such as '1: Yes, 2: no'",
			"options": {
				"1": { "text":"yes", "nextnode":"2"},
				"2": { "text":"no", "nextnode":"3"},
			}
		},
		"2":{
			"textbody": "Notice how I don't have an optionbody or options, that means when you reach me... \nGame over."
		},
        "3":{
			"textbody": "I am also... \nGame over."
		}
    }
}
```
### Attribute meanings: 
- **game** specifies that this is the game being played. 
- **0** is a story node indicator, "0" is a special indicator, because it is *the first* storyNode main.py will look for. 
- **textbody** is what the user will see, this is the game itself. 
  - 'you wander to the mouth of a forest...'
- **optionbody** is what the user will see regarding options, 
  - '1: Yes, 2: no'
- **options** maps the user input to the different nodes. 
  - The **"1"** indicates what the user will input, in this instance we expect the user to input 1 or 2. 
  - **text** is what the user sees to select that option. While this isn't neccessary to run, it is helpful to keep track of the mappings and improves readability. 
  - **nextnode** is what actually maps the user selection to the next node. This is so that once there are more options, the user can still select 1 or 2, and actually navigate to nodes greater than 1 or 2. Notice in the example how user selecting '2' will actually jump to storynode 3. 
- **"2"** and **"3"** is also a story node indicator, and they can be configured like any other storynode with an optionbody and textbody. 

## game.json 
Is a simple game file example using the format specified above. It is effectively an n-ary tree data structure due to the options mapping and contains no loops. 

## config.json 
A JSON file used to configure main.py. Currently it only has one attribute, **"gamefile"** which is used to select the gamefile to read. There is no need to change any code in order to redirect to a different game file. 

## main.py 
The main.py file's purpose is to read the config file, the read from the specified game file, and parse the text game. It will load each storynode individually as needed, so if a branch is not traversesd, it will not be loaded into a storyNode object instance. 

