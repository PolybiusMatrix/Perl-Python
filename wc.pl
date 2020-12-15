#!/usr/bin/perl

use strict;
use warnings;

my %counter;
my $linecount;
my $wordcount = 0;
my $charcount;

my $file = shift or die;
open my $fh, '<', $file or die, "Cannot open '$file' $!";
while ( my $line = <$fh> ){
	$linecount++;
	$charcount += length($line);
	#$wordcount += scalar(split(/\s+/, $_));
	chomp $line;
	foreach my $string( $line =~ /\w+/g ){
		$counter{$string}++;
	}
}

print "Number of characters: $charcount\n";
print "Number of words: $wordcount\n";
print "Number of lines: $linecount\n";
print "Frequency of words in the file:\n";
print "---------------------------------\n";
foreach my $string( sort keys %counter ){
	$wordcount++;
	printf "%s: %s\n", $string, $counter{$string};
}
