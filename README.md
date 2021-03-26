# NEU-CS5001-Final-Project
A memory matching card game!

Background:
This was created in the fall of 2021 for my final project in CS 5001.

Launch:
Run the PlayGame.py file 

Overview:
It is a memory matching game! The cards are flipped over so you can't see their designed, and each turn you select two cards to try and match them. If they 
matched, they are taken off the board. The goal is to clear the board in a few turns as possible and the top 6 scores are recorded on the score board.

Known Bugs:
- Not technically a bug, it isn't fully implemented with good object oriented design. Though I creaded some class objects, they don't package their
own data and I relied on some global variables instead. 
- The game comes with the option to upload your own jpegs to use as the card faces. I haven't yet figured out a way to automatically rezise images, however, so 
if the images you choose are not the size the board expexts, the game can still be played; it just has a really bad GUI as the cards take up more space than
their button areas are registered for.
