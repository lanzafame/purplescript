
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\xb8\x1c\xb7(y%+D\xdb\x8e\x92\xe7\x17\xc52\xb2'
    
_lr_action_items = {'LBRACE':([7,8,9,10,11,12,13,14,15,16,18,20,26,28,30,],[-18,-11,12,-6,-9,-18,-5,-17,-8,-7,12,-10,-18,12,-16,]),'END':([10,11,13,14,15,16,20,26,28,30,],[-6,-9,-5,-17,-8,-7,-10,-18,30,-16,]),'RBRACE':([10,11,12,13,14,15,16,18,20,30,],[-6,-9,-18,-5,-17,-8,-7,20,-10,-16,]),'ENDCLASS':([7,8,9,10,11,13,14,15,16,20,30,],[-18,-11,14,-6,-9,-5,-17,-8,-7,-10,-16,]),'COMMA':([21,22,23,24,25,29,],[-18,27,-12,-15,-14,-13,]),'LPAREN':([8,19,],[-11,21,]),'VARIABLE':([5,17,21,27,],[8,8,23,23,]),'RPAREN':([21,22,23,24,25,29,],[-18,26,-12,-15,-14,-13,]),'CLASS':([0,1,3,4,6,7,8,9,10,11,12,13,14,15,16,18,20,26,28,30,],[-18,5,-3,-4,-2,-18,-11,5,-6,-9,-18,-5,-17,-8,-7,5,-10,-18,5,-16,]),'DEF':([7,8,9,10,11,12,13,14,15,16,18,20,26,28,30,],[-18,-11,17,-6,-9,-18,-5,-17,-8,-7,17,-10,-18,17,-16,]),'$end':([0,1,2,3,4,6,14,],[-18,-1,0,-3,-4,-2,-17,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'class_declaration_statement':([1,9,18,28,],[4,11,11,11,]),'inner_statement':([9,18,28,],[13,13,13,]),'parameter_list':([21,],[22,]),'start':([0,],[2,]),'variable':([5,17,],[7,19,]),'empty':([0,7,12,21,26,],[3,10,10,24,10,]),'statement':([9,18,28,],[16,16,16,]),'top_statement_list':([0,],[1,]),'parameter':([21,27,],[25,29,]),'inner_statement_list':([7,12,26,],[9,18,28,]),'top_statement':([1,],[6,]),'function_declaration_statement':([9,18,28,],[15,15,15,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> top_statement_list','start',1,'p_start','parser.py',24),
  ('top_statement_list -> top_statement_list top_statement','top_statement_list',2,'p_top_statement_list','parser.py',28),
  ('top_statement_list -> empty','top_statement_list',1,'p_top_statement_list','parser.py',29),
  ('top_statement -> class_declaration_statement','top_statement',1,'p_top_statement','parser.py',37),
  ('inner_statement_list -> inner_statement_list inner_statement','inner_statement_list',2,'p_inner_statement_list','parser.py',45),
  ('inner_statement_list -> empty','inner_statement_list',1,'p_inner_statement_list','parser.py',46),
  ('inner_statement -> statement','inner_statement',1,'p_inner_statement','parser.py',53),
  ('inner_statement -> function_declaration_statement','inner_statement',1,'p_inner_statement','parser.py',54),
  ('inner_statement -> class_declaration_statement','inner_statement',1,'p_inner_statement','parser.py',55),
  ('statement -> LBRACE inner_statement_list RBRACE','statement',3,'p_statement_block','parser.py',60),
  ('variable -> VARIABLE','variable',1,'p_variable','parser.py',65),
  ('parameter -> VARIABLE','parameter',1,'p_parameter','parser.py',70),
  ('parameter_list -> parameter_list COMMA parameter','parameter_list',3,'p_parameter_list','parser.py',74),
  ('parameter_list -> parameter','parameter_list',1,'p_parameter_list','parser.py',75),
  ('parameter_list -> empty','parameter_list',1,'p_parameter_list','parser.py',76),
  ('function_declaration_statement -> DEF variable LPAREN parameter_list RPAREN inner_statement_list END','function_declaration_statement',7,'p_function_declaration_statement','parser.py',83),
  ('class_declaration_statement -> CLASS variable inner_statement_list ENDCLASS','class_declaration_statement',4,'p_class_declaration_statement','parser.py',88),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',92),
]
