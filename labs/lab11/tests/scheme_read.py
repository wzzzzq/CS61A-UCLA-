test = {
  'name': 'scheme_read',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> scheme_read(Buffer(tokenize_lines(['nil'])))
          nil
          >>> scheme_read(Buffer(tokenize_lines(['1'])))
          1
          >>> scheme_read(Buffer(tokenize_lines(['true'])))
          True
          >>> read_tail(Buffer(tokenize_lines(['2)'])))
          Pair(2, nil)
          >>> read_tail(Buffer(tokenize_lines(['(2)'])))
          SyntaxError
          >>> read_line('3')
          3
          >>> read_line('-123')
          -123
          >>> read_line('1.25')
          1.25
          >>> read_line('true')
          True
          >>> read_line('(a)')
          Pair('a', nil)
          >>> read_line(')')
          SyntaxError
          >>> read_line('(a))')
          SyntaxError
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> tokens = tokenize_lines(["(+ 1 ", "(23 4)) ("])
          >>> src = Buffer(tokens)
          >>> src.current
          '('
          >>> src.pop_first()
          '('
          >>> src.current
          '+'
          >>> src.pop_first()
          '+'
          >>> src.pop_first()
          1
          >>> src.current
          This is a token representing the end of a line.
          >>> src.end_of_line()
          True
          >>> src.pop_first()
          This is a token representing the end of a line.
          >>> scheme_read(src)  # Removes the next complete expression in src and returns it as a Pair
          Pair(23, Pair(4, nil))
          >>> src.current
          ')'
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> scheme_read(Buffer(tokenize_lines(['(18 6)']))) # Type SyntaxError if you think this errors
          b9d5823db55af0cd048a061f6dcfb3d1
          # locked
          >>> read_line('(18 6)')  # Shorter version of above!
          b9d5823db55af0cd048a061f6dcfb3d1
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> read_tail(Buffer(tokenize_lines([')'])))
          b0f31f4d3b6358d261ea505f9eb2b934
          # locked
          >>> read_tail(Buffer(tokenize_lines(['1 2 3)'])))
          c8c1ed2d80f1a2a4c91a49e95404d13b
          # locked
          >>> read_tail(Buffer(tokenize_lines(['2 (3 4))'])))
          e0fa6fce82a72c162a31227fd396f553
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> read_tail(Buffer(tokenize_lines(['(1 2 3)']))) # Type SyntaxError if you think this errors
          c879c61b05fa3a9a49fdb999db4c9c9f
          # locked
          >>> read_line('((1 2 3)') # Type SyntaxError if you think this errors
          c879c61b05fa3a9a49fdb999db4c9c9f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> src = Buffer(tokenize_lines(["(+ 1 2)"]))
          >>> scheme_read(src)
          Pair('+', Pair(1, Pair(2, nil)))
          >>> src.current
          This is a token representing the end of a line.
          >>> src.pop_first()
          This is a token representing the end of a line.
          >>> src.current # Don't forget to remove the closing parenthesis!
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> read_line("(+ (- 2 3) 1)")
          bf1795a56ce544a74a4d22988ad22865
          # locked
          # choice: Pair('+', Pair('-', Pair(2, Pair(3, Pair(1, nil)))))
          # choice: Pair('+', Pair('-', Pair(2, Pair(3, nil))), Pair(1, nil))
          # choice: Pair('+', Pair(Pair('-', Pair(2, Pair(3, nil))), Pair(1, nil)))
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> read_line("()")
          nil
          >>> read_line("((a))")
          Pair(Pair('a', nil), nil)
          >>> read_line("(+ 1 (- 2 3) 8)")
          Pair('+', Pair(1, Pair(Pair('-', Pair(2, Pair(3, nil))), Pair(8, nil))))
          # choice: Pair('+', Pair(1, Pair('-', Pair(2, 3), Pair(8, nil))))
          # choice: Pair('+', Pair(1, Pair(Pair('-', Pair(2, 3)), Pair(8, nil))))
          # choice: Pair('+', Pair(1, Pair('-', Pair(2, Pair(3, nil)), Pair(8, nil))))
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> from scheme_reader import *
      """,
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
