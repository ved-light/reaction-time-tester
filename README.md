# Reaction Time Tester

## Overview
[cite_start]A Python-based command-line application designed to measure and quantify an user's reaction speed to an visual stimulas[cite: 89, 90].

## Features
* **Randomized Delays:** Uses random intervals (2-8 seconds) to prevent prediction.
* **Early Detection:** Disqualifies users who press keys before the signal.
* **Precision Timing:** Calculates reaction time to a 4 decimal places.
* [cite_start]**Replay Loop:** Allows continuous testing without restarting the script[cite: 92].

## Technologies Used
* **Language:** Python 3
* [cite_start]**Libraries:** `time` (timing), `random` (delays), `msvcrt` (Windows console input)[cite: 93].

## Steps to Install & Run
1.  Ensure Python 3 is installed.
2.  Ensure you are using a Windows Operating System (due to `msvcrt` dependency).
3.  Download `source-code.py`.
4.  Open a terminal/command prompt.
5.  [cite_start]Run the command: `python source-code.py`[cite: 94].

## Instructions for Testing
1.  Start the program.
2.  Press `ENTER` to begin the sequence.
3.  Wait for the "GO!!!" text.
4.  Press `ENTER` immediately.
5.  View your reaction time in seconds.
6.  [cite_start]Type 'y' to retry or 'n' to exit[cite: 95].