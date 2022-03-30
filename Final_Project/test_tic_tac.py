# from tic_tac_toe import add_number, drawBoard, drawO, drawX, activate, deactivate, addX
from tic_tac_toe import *

import pytest
# from pytest import approx


def test_add_number():
    assert addNumber() == True

def test_drawBoard():
    assert drawBoard() == True

def test_drawO():
    assert drawO(0,0) == True

def test_drawX():
    assert drawX(0,0) == True

def test_activate():
    def squareOne():
        addX(0, 0)
    def squareTwo():
        addX(0, 1)
    def squareThree():
        addX(0, 2)
    def squareFour():
        addX(1, 0)
    def squareFive():
        addX(1, 1)
    def squareSix():
        addX(1, 2)
    def squareSeven():
        addX(2, 0)
    def squareEight():
        addX(2, 1)
    def squareNine():
        addX(2, 2)
    functions = [squareOne, squareTwo, squareThree, 
    squareFour, squareFive, squareSix, squareSeven, 
    squareEight, squareNine]
    assert activate(functions) == True

def test_deactivate():
    assert deactivate() == True

def test_addX():
    assert addX(0, 0) == True

def test_addO():
    assert addO() == None

def test_checkWon():
    assert checkWon("o") == False

def test_checkTie():
    assert checkTie() == False