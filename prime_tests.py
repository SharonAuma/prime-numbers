#Tests correct output for larger input
   def test_prime_generator_large_input(self):
       self.assertEqual(prime_generator(100),[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

 #Test for negtive input
       def test_prime_generator_negative_input(self):
       self.assertEqual(prime_generator(-10),"Error wrong input"


 #Test for negtive input
      def test_prime_generator_negative_input(self):
       self.assertEqual(prime_generator(-20),"Error wrong input"

  #Tests correct output for larger input
   def test_prime_generator_small_input(self):
       self.assertEqual(prime_generator(20),[2, 3, 5, 7, 11, 13, 17, 19])

 #Tests correct output for larger input
   def test_prime_generator_large_input(self):
       self.assertEqual(prime_generator(30),[2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
