#!/usr/bin/env python

import argparse
import sys
import os

import argparse

parser=argparse.ArgumentParser(description="fill in a madlib")
parser.add_argument('move_by_p1', 
	choices=['rock', 'paper', 'scissors'],
	help="person1 choice of rock, paper, or scissors")
parser.add_argument('move_by_p2', 
	choices=['rock', 'paper', 'scissors'],
	help="person2 choice of rock, paper, or scissors")
parser.add_argument("--names","-n", type=str, nargs=2, 
	required=True,
	help="Two peoples name. They cannot be the same name.")
parser.add_argument("--ages","-a", type=int, nargs=2, 
	required=False,
	help="Two peoples age.")
args=parser.parse_args()

# Write statement of who wins rock, paper, scissors
#	winner_name: persons name who wins
#	loser_name: persons name who loses
#	winning_move: move that wins the game
#	losing_move: move the loses the game
def game_output(winner_name, loser_name, winning_move, losing_move):
	if winning_move == losing_move: # account for a tie
		return("Both chose %s and they tied.\n" % args.move_by_p1)
	else:
		return("%s chose %s and %s chose %s. %s won.\n\n" 
				% (winner_name, winning_move,
					loser_name, losing_move,
					winner_name))

# Exit if person names are not different
if args.names[0] == args.names[1]:
	sys.exit(">>> ERROR: people argument cannot have the same name")

# Begin madlibs story
sys.stdout.write("\n%s and %s are friends.\n" % \
	(args.names[0], args.names[1]))

# If set, state peoples ages
if args.ages:
	sys.stdout.write("%s is %i years old.\n" % \
	(args.names[0], args.ages[0]))
	sys.stdout.write("%s is %i years old.\n" % \
	(args.names[1], args.ages[1]))

# Play game
sys.stdout.write("They decide to play rock, paper, scissors.\n")
game_decision=""
if args.move_by_p1 == args.move_by_p2:
	game_decision = game_output(args.names[0], args.names[1], 
		args.move_by_p1, args.move_by_p2)
else:
	if args.move_by_p1 == "rock":
		if args.move_by_p2 == "paper":
			game_decision = game_output(args.names[1], args.names[0], 
				"paper", "rock")
		else:
			game_decision = game_output(args.names[0], args.names[1], 
				"rock", "scissors")
	elif args.move_by_p1 == "paper":
		if args.move_by_p2 == "rock":
			game_decision = game_output(args.names[0], args.names[1], 
				"paper", "rock")
		else:
			game_decision = game_output(args.names[1], args.names[0], 
				"scissors", "paper")
	else:
		if args.move_by_p2 == "paper":
			game_decision = game_output(args.names[0], args.names[1], 
				"scissors", "paper")
		else:
			game_decision = game_output(args.names[1], args.names[0], 
				"rock", "scissors")

sys.stdout.write(game_decision)