#!/usr/bin/perl

use strict;
use warnings;

my $exit = "quit";
my $uInp;
my $substr;
my $lowercase; 	#to be used for the comparison for palindrome

#print "String: $uInp"	#just to test output

	do{
		print "Please input a string: ";
		chomp($uInp = readline(STDIN));
		$lowercase = lc($uInp);

		if ( $lowercase eq reverse($lowercase) ){
			print "$uInp IS a palindrome!\n";
		}
		
		elsif ( $lowercase eq $exit ){
			#Keyword "last" quit on a warning, so an empty block of code seemed to get the job done
			#Why wouldn't 'last' work in this instance?			
		}
	
		else {
			print "$uInp IS NOT a palindrome.\n";
		}

	}until( $lowercase eq $exit );


