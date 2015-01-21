Bret Runestad
currency conversion assignment

The convert function takes a list of rates, a starting value, and two strings: a 'from' string and a 'two' string.  The list of rates must take the form of a list of tuples.  Each tuple should take the form ('USD', 'EUR', 0.74), where the first two indexes are 3-letter codes for different currencies, and the 3rd index is the conversion rate from the first code to the second.  The 'from' and 'to' strings must be 3-letter codes that correspond to existing pairs within the list of rates, although the order of the pair may be reversed.  When run, the convert function will take the starting value, and convert that amount from the 'from' currency to the 'to' currency.  It is as fun as it sounds.

The exception_check program is a small program whose sole purpose is to catch the IndexError that arises when the 'from' and 'to' strings do not match with a corresponding tuple.
