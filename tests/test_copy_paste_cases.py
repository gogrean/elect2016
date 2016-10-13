TESTS = [('"@bla blub" toehtaou', True),
         ('"@bla blub teueieoi', True),
         ('"etuhothi" eotuheoti', False),
         ('@bla ehuteohuteoi', False),
         ('@bla eihetihetdi" euheoti', True),
         ('@blao eihetihidt "eiuiuid"', False),
         ('@blaou ouoeiei" ieuidued"', False),
         ('@eoeiei eieia eiiei " eoiheoi"', True),
         ('@ueoueou eueu" oeueou "eueou" eueoueou"', False),
         ('Thanks for supporting me @oetiuteohi eueu" dehuidhoi', True),
         ('Beoruoeu "uueu @oeuoei euei" eieoi', False),
         ('Nice! "@uaduipdi."', True),
         ('Nice! @upaip.ai"', True),
         ('@uhaphdup uupa"upy3y', True)]


