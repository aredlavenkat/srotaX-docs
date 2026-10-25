# Operator behavior reference

**159 registered expression operators**, documented from 6,495 executed cases.

[Read the coverage and testing methodology](operator-parity.md).

Each page separates SrotaX behavior from an optional MongoDB comparison section. The input tables are concrete regression cases, not a claim that every possible combination has been tested.

| Operator | Purpose | Cases |
| --- | --- | --- |
| [$abs](operators/abs.md) | Returns absolute magnitude. | 22 |
| [$acos](operators/acos.md) | Computes inverse cosine. | 22 |
| [$acosh](operators/acosh.md) | Computes inverse hyperbolic cosine. | 22 |
| [$add](operators/add.md) | Adds numbers, or adds millisecond offsets to a single date. | 43 |
| [$allElementsTrue](operators/allElementsTrue.md) | Tests whether every array value is truthy under Fluxion coercion. | 22 |
| [$and](operators/and.md) | Requires all expression results to be truthy. | 41 |
| [$anyElementTrue](operators/anyElementTrue.md) | Tests whether any array value is truthy under Fluxion coercion. | 22 |
| [$arrayElemAt](operators/arrayElemAt.md) | Reads an array item at a positive or negative index. | 42 |
| [$arrayToObject](operators/arrayToObject.md) | Converts key/value entries into an object. | 22 |
| [$asin](operators/asin.md) | Computes inverse sine. | 22 |
| [$asinh](operators/asinh.md) | Computes inverse hyperbolic sine. | 22 |
| [$atan](operators/atan.md) | Computes inverse tangent. | 22 |
| [$atan2](operators/atan2.md) | Computes two-argument inverse tangent. | 41 |
| [$atanh](operators/atanh.md) | Computes inverse hyperbolic tangent. | 22 |
| [$avg](operators/avg.md) | Averages numeric values from one array expression or explicit operands; ignores nonnumeric values. | 60 |
| [$binarySize](operators/binarySize.md) | Counts bytes in text or supported binary values. | 22 |
| [$bitAnd](operators/bitAnd.md) | Computes bitwise AND of integers. | 41 |
| [$bitNot](operators/bitNot.md) | Flips int32 or int64 bits, preserving integer width. | 37 |
| [$bitOr](operators/bitOr.md) | Computes bitwise OR of integers. | 41 |
| [$bitXor](operators/bitXor.md) | Computes bitwise exclusive OR of integers. | 41 |
| [$bsonSize](operators/bsonSize.md) | Returns the actual BSON-encoded document size in bytes, or null for null input. | 22 |
| [$ceil](operators/ceil.md) | Rounds upward to a whole number. | 22 |
| [$cmp](operators/cmp.md) | Returns the ordering of two values. | 41 |
| [$coalesce](operators/coalesce.md) | Returns the first non-null expression. | 41 |
| [$concat](operators/concat.md) | Concatenates strings, skipping null operands. | 41 |
| [$concatArrays](operators/concatArrays.md) | Concatenates arrays. | 41 |
| [$cond](operators/cond.md) | Evaluates Mongo truthiness and lazily returns the selected branch. | 61 |
| [$convert](operators/convert.md) | Converts input to a named target type with optional fallbacks. | 123 |
| [$cos](operators/cos.md) | Computes cosine. | 22 |
| [$cosh](operators/cosh.md) | Computes hyperbolic cosine. | 22 |
| [$dateAdd](operators/dateAdd.md) | Adds a calendar amount and returns a date value. | 83 |
| [$dateDiff](operators/dateDiff.md) | Counts elapsed whole units between dates. | 103 |
| [$dateFromParts](operators/dateFromParts.md) | Builds a date value from calendar parts. | 223 |
| [$dateFromString](operators/dateFromString.md) | Parses a date string and returns a date value. | 103 |
| [$dateSubtract](operators/dateSubtract.md) | Subtracts a calendar amount and returns a date value. | 83 |
| [$dateToParts](operators/dateToParts.md) | Extracts calendar fields into an object. | 63 |
| [$dateToString](operators/dateToString.md) | Formats a typed date using Mongo 6 numeric format tokens. | 83 |
| [$dateTrunc](operators/dateTrunc.md) | Truncates a date and returns a date value. | 103 |
| [$dayOfMonth](operators/dayOfMonth.md) | Extracts day of month using the host calendar. | 22 |
| [$dayOfWeek](operators/dayOfWeek.md) | Extracts day of week using the host calendar. | 22 |
| [$dayOfYear](operators/dayOfYear.md) | Extracts day of year using the host calendar. | 22 |
| [$degreesToRadians](operators/degreesToRadians.md) | Computes conversion from degrees to radians. | 22 |
| [$divide](operators/divide.md) | Divides the first numeric operand by the second. | 42 |
| [$endsWith](operators/endsWith.md) | Checks a literal text suffix. | 41 |
| [$eq](operators/eq.md) | Tests equality using BSON-aware comparison. | 41 |
| [$exp](operators/exp.md) | Raises e to the supplied exponent. | 22 |
| [$expr](operators/expr.md) | Evaluates an expression as a Fluxion passthrough extension. | 22 |
| [$filter](operators/filter.md) | Keeps array elements satisfying a boolean condition. | 64 |
| [$first](operators/first.md) | Reads the first array element. | 22 |
| [$firstN](operators/firstN.md) | Returns a new array without changing the source list. | 43 |
| [$floor](operators/floor.md) | Rounds downward to a whole number. | 22 |
| [$function](operators/function.md) | Executes a JavaScript function in a restricted GraalJS context. | 61 |
| [$getField](operators/getField.md) | Reads a named field from an explicit object. | 44 |
| [$gt](operators/gt.md) | Tests whether the first value is greater. | 41 |
| [$gte](operators/gte.md) | Tests whether the first value is greater or equal. | 41 |
| [$hour](operators/hour.md) | Extracts hour using the host calendar. | 22 |
| [$ifNull](operators/ifNull.md) | Uses a fallback when the first expression is null or missing. | 41 |
| [$in](operators/in.md) | Tests membership in an array without flattening the searched value. | 41 |
| [$indexOfArray](operators/indexOfArray.md) | Finds an item using Java equality. | 41 |
| [$indexOfBytes](operators/indexOfBytes.md) | Searches text using byte positions; bounds have known differences. | 41 |
| [$indexOfCP](operators/indexOfCP.md) | Searches text using Unicode code-point positions. | 41 |
| [$isArray](operators/isArray.md) | Tests whether a value is an array. | 22 |
| [$isNumber](operators/isNumber.md) | Tests whether a value is numeric. | 22 |
| [$isoDayOfWeek](operators/isoDayOfWeek.md) | Extracts iso day of week using the host calendar. | 22 |
| [$isoWeek](operators/isoWeek.md) | Extracts iso week using the host calendar. | 22 |
| [$isoWeekYear](operators/isoWeekYear.md) | Extracts iso week year using the host calendar. | 22 |
| [$last](operators/last.md) | Reads the last array element. | 22 |
| [$lastN](operators/lastN.md) | Returns a new array without changing the source list. | 43 |
| [$let](operators/let.md) | Evaluates an expression with locally bound variables. | 44 |
| [$literal](operators/literal.md) | Returns a value without evaluating it. | 21 |
| [$ln](operators/ln.md) | Computes the natural logarithm. | 22 |
| [$log](operators/log.md) | Computes a logarithm using the supplied base. | 41 |
| [$log10](operators/log10.md) | Computes the base-ten logarithm. | 22 |
| [$lt](operators/lt.md) | Tests whether the first value is less. | 41 |
| [$lte](operators/lte.md) | Tests whether the first value is less or equal. | 41 |
| [$ltrim](operators/ltrim.md) | Trims configured characters from the start of text. | 43 |
| [$map](operators/map.md) | Evaluates an expression for each array element. | 63 |
| [$max](operators/max.md) | Returns the maximum non-null value from one array expression or explicit operands. | 60 |
| [$maxN](operators/maxN.md) | Returns a new array without changing the source list. | 43 |
| [$median](operators/median.md) | Computes single-document statistics, ignoring nonnumeric values. | 59 |
| [$mergeObjects](operators/mergeObjects.md) | Combines objects with later values replacing earlier fields. | 41 |
| [$millisecond](operators/millisecond.md) | Extracts millisecond using the host calendar. | 22 |
| [$min](operators/min.md) | Returns the minimum non-null value from one array expression or explicit operands. | 60 |
| [$minDistance](operators/minDistance.md) | Computes minimum planar or spherical distance to supplied points. | 63 |
| [$minN](operators/minN.md) | Returns a new array without changing the source list. | 43 |
| [$minute](operators/minute.md) | Extracts minute using the host calendar. | 22 |
| [$mod](operators/mod.md) | Returns the numeric remainder. | 41 |
| [$month](operators/month.md) | Extracts month using the host calendar. | 22 |
| [$multiply](operators/multiply.md) | Multiplies numeric operands. | 41 |
| [$ne](operators/ne.md) | Tests inequality using BSON-aware comparison. | 41 |
| [$nin](operators/nin.md) | Negates array membership. | 41 |
| [$nor](operators/nor.md) | Negates a disjunction. | 41 |
| [$not](operators/not.md) | Negates one expression result. | 22 |
| [$objectToArray](operators/objectToArray.md) | Converts object fields to key/value entries. | 22 |
| [$or](operators/or.md) | Requires at least one truthy expression result. | 41 |
| [$percentile](operators/percentile.md) | Computes single-document statistics, ignoring nonnumeric values. | 86 |
| [$pow](operators/pow.md) | Raises the first number to the second power. | 41 |
| [$radiansToDegrees](operators/radiansToDegrees.md) | Computes conversion from radians to degrees. | 22 |
| [$range](operators/range.md) | Generates numbers from an inclusive start to an exclusive end. | 41 |
| [$reduce](operators/reduce.md) | Folds an array into an accumulated value. | 64 |
| [$regexFind](operators/regexFind.md) | Finds the first regex match and its UTF-16 index. | 63 |
| [$regexFindAll](operators/regexFindAll.md) | Finds regex matches and their UTF-16 indexes. | 63 |
| [$regexMatch](operators/regexMatch.md) | Tests whether a Java regular expression matches text. | 64 |
| [$replaceAll](operators/replaceAll.md) | Replaces all literal text occurrences. | 63 |
| [$replaceOne](operators/replaceOne.md) | Replaces the first literal text occurrence. | 63 |
| [$reverseArray](operators/reverseArray.md) | Reverses array elements. | 22 |
| [$round](operators/round.md) | Rounds a number to the specified decimal place using ties-to-even rounding (HALF_EVEN); the place defaults to zero. | 24 |
| [$rtrim](operators/rtrim.md) | Trims configured characters from the end of text. | 43 |
| [$second](operators/second.md) | Extracts second using the host calendar. | 22 |
| [$setDifference](operators/setDifference.md) | Returns values from the first set absent from the second. | 41 |
| [$setEquals](operators/setEquals.md) | Tests unordered set equality. | 41 |
| [$setField](operators/setField.md) | Sets a named field on an object copy. | 63 |
| [$setIntersection](operators/setIntersection.md) | Returns common distinct array values; zero arguments return an empty array. | 47 |
| [$setIsSubset](operators/setIsSubset.md) | Tests whether the first set is contained in the second. | 41 |
| [$setIsSuperset](operators/setIsSuperset.md) | Tests whether the first set contains the second. | 41 |
| [$setUnion](operators/setUnion.md) | Returns distinct combined array values. | 41 |
| [$sin](operators/sin.md) | Computes sine. | 22 |
| [$sinh](operators/sinh.md) | Computes hyperbolic sine. | 22 |
| [$size](operators/size.md) | Counts elements of an array. | 22 |
| [$slice](operators/slice.md) | Extracts an array segment; negative indexes are not Mongo-compatible. | 60 |
| [$sortArray](operators/sortArray.md) | Returns a new array without changing the source list. | 42 |
| [$split](operators/split.md) | Splits text using a Java regular-expression delimiter. | 41 |
| [$sqrt](operators/sqrt.md) | Computes the square root. | 23 |
| [$startsWith](operators/startsWith.md) | Checks a literal text prefix. | 41 |
| [$stdDevPop](operators/stdDevPop.md) | Computes single-document statistics, ignoring nonnumeric values. | 81 |
| [$stdDevSamp](operators/stdDevSamp.md) | Computes single-document statistics, ignoring nonnumeric values. | 81 |
| [$strLenBytes](operators/strLenBytes.md) | Counts UTF-8 bytes in a string. | 22 |
| [$strLenCP](operators/strLenCP.md) | Counts Unicode code points in a string. | 22 |
| [$strcasecmp](operators/strcasecmp.md) | Compares lower-cased strings. | 41 |
| [$substr](operators/substr.md) | Extracts a substring using UTF-16 indexes. | 60 |
| [$substrBytes](operators/substrBytes.md) | Extracts text from a UTF-8 byte range. | 60 |
| [$substrCP](operators/substrCP.md) | Extracts text using Unicode code-point indexes. | 60 |
| [$subtract](operators/subtract.md) | Subtracts numbers, subtracts a millisecond offset from a date, or returns the millisecond difference between two dates. | 41 |
| [$sum](operators/sum.md) | Sums numeric values from one array expression or explicit operands; ignores nonnumeric values. | 60 |
| [$switch](operators/switch.md) | Selects the first branch with a true boolean condition. | 43 |
| [$tan](operators/tan.md) | Computes tangent. | 22 |
| [$tanh](operators/tanh.md) | Computes hyperbolic tangent. | 22 |
| [$toArray](operators/toArray.md) | Parses a strict JSON string into an array. | 41 |
| [$toBool](operators/toBool.md) | Converts a value to bool. | 22 |
| [$toDate](operators/toDate.md) | Converts a value to date. | 22 |
| [$toDecimal](operators/toDecimal.md) | Converts a value to decimal. | 22 |
| [$toDouble](operators/toDouble.md) | Converts a value to double. | 22 |
| [$toInt](operators/toInt.md) | Converts a value to int. | 22 |
| [$toLong](operators/toLong.md) | Converts a value to long. | 22 |
| [$toLower](operators/toLower.md) | Converts text to lower case. | 22 |
| [$toObject](operators/toObject.md) | Parses a strict JSON string into an object. | 41 |
| [$toObjectId](operators/toObjectId.md) | Converts a value to objectid. | 22 |
| [$toString](operators/toString.md) | Converts a value to a string. | 22 |
| [$toUpper](operators/toUpper.md) | Converts text to upper case. | 22 |
| [$topN](operators/topN.md) | Sort an array and return its first N items without changing the source. | 62 |
| [$trim](operators/trim.md) | Trims configured characters from both ends of text. | 43 |
| [$trunc](operators/trunc.md) | Truncates a number to an optional decimal place. | 41 |
| [$tsIncrement](operators/tsIncrement.md) | Reads increment from a Fluxion timestamp map. | 22 |
| [$tsSecond](operators/tsSecond.md) | Reads seconds from a Fluxion timestamp map. | 22 |
| [$type](operators/type.md) | Returns the BSON-style type name of a value. | 22 |
| [$unsetField](operators/unsetField.md) | Removes a named field from an object copy. | 43 |
| [$week](operators/week.md) | Extracts week using the host calendar. | 22 |
| [$year](operators/year.md) | Extracts year using the host calendar. | 22 |
| [$zip](operators/zip.md) | Combines corresponding elements of input arrays. | 42 |
