#!/usr/bin/env ruby
puts ARGV[0].scan(/from:(\+?\d+|[A-Za-z]*).*to:(\+?\d+)].*flags:(-?\d:-?\d:-?\d:-?\d:-?\d)/).join(',')