# -----------------------------------------------------------------------------
# purplescript:lexer.py
#
# Copyright (C) 2010,
# Martin Rusev
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# * Redistributions of source code must retain the above copyright notice,
#   this list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# * Neither the name of the author nor the names of other
#   contributors may be used to endorse or promote products derived
#   from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# -----------------------------------------------------------------------------

__version__ = '0.1'
__all__ = ['get_tokens']

import ply.lex as lex
from helper import *
#get_tokens
import os.path
import sys

reserved_words = {
   'if' : 'IF',
   'elseif': 'ELSEIF',
   'else' : 'ELSE',
   'endif': 'ENDIF',
   'for': 'FOR',
   'in': 'IN',
   'endfor': 'ENDFOR',
   'end' : 'END',
   'endclass' : 'ENDCLASS',
   'def' : 'DEF',
   'class' : 'CLASS'
}

operators = (
    'ASSIGNMENT',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'MODULO',
    'OR', 'AND', 'NOT', 'LT', 'LE', 'GT', 'GE',
    'EQ', 'NE',
)

delimiters = (
  'LPAREN', 'RPAREN', 'LBRACKET',
  'RBRACKET', 'ARRAY_BEGIN', 'ARRAY_END',
  'COMMA', 'SEMI', 'COLON', 'DOT',
)

increment_decrement = (
    'INCREMENT', 'DECREMENT',
)

object_oriented =(
   'THIS',
)

data_types = (
  'STRING',
)

generic_tokens = (
   'COMMENT', 'VARIABLE',
)

tokens = merge_lists(
       operators, delimiters, object_oriented,
       increment_decrement, data_types, generic_tokens,
       reserved_words.values(),
)


# OPERATORS
t_ASSIGNMENT       = r'='
t_PLUS             = r'\+'
t_MINUS            = r'-'
t_TIMES            = r'\*'
t_DIVIDE           = r'/'
t_MODULO           = r'%'
t_OR               = r'\|\|'
t_AND              = r'&&'
t_NOT              = r'!'
t_LT               = r'<'
t_GT               = r'>'
t_LE               = r'<='
t_GE               = r'>='
t_EQ               = r'=='
t_NE               = r'!='


# DELIMITERS
t_LPAREN           = r'\('
t_RPAREN           = r'\)'
t_LBRACKET         = r'\['
t_RBRACKET         = r'\]'
t_ARRAY_BEGIN      = r'\{'
t_ARRAY_END        = r'\}'
t_COMMA            = r','
t_SEMI             = r';'
t_COLON            = r':'
t_DOT              = r'\.'


# Increment/decrement
t_INCREMENT        = r'\+\+'
t_DECREMENT        = r'--'

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved_words.get(t.value,'VARIABLE')
    return t

# OBJECT ORIENTED
def t_THIS(t):
    ur'@+'
    return t

# DATA TYPES
def t_STRING(t):
    ur"'\w+'"
    return t

def t_newline(t):
    ur'\n+'
    t.lexer.lineno += t.value.count("\n")

t_ignore  = '\n\t'

def t_error(t):
    #print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

def t_COMMENT(t):
    r'//.*\n'
    t.lexer.lineno += 1
    return t




def get_tokens(file=None, *args, **kwargs):

    lexer = lex.lex()
    try:
        os.path.isfile(file)
        with open(file, 'r') as f:
             data = f.read()
             lexer.input(data)
        return lexer
    except:
        #print "Error in lexer.py line 170:", sys.exc_type, ":", sys.exc_value
        print "(error lexer.py:170)The file {file} doen't exists".format(file=file)

if __name__ == '__main__':

    lexer = lex.lex()

    with open('syntax.txt', 'r') as f:
         data = f.read()
         lexer.input(data)

         while True:
               tok = lexer.token()
               if not tok: break
               print tok



