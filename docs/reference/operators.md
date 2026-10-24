# Operator inventory

Catalog snapshot: **146 registered engine operators**, **119 Visual function entries**. Target metadata: MongoDB 6.0.

Registration is not the same as compiler acceptance, Visual availability, or verified MongoDB parity. The compiler validates the complete expression and its field types. The tested-example column refers only to the checked-in compiler/engine example, not all inputs.

| Operator | Category | Visual entry | Example executed | Metadata classification |
| --- | --- | --- | --- | --- |
| [$abs](operators/abs.md) | Arithmetic | Yes | Yes | MONGO_6_DIFFERENCES |
| [$acos](operators/acos.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$acosh](operators/acosh.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$add](operators/add.md) | Arithmetic | Yes | Yes | MONGO_6_DIFFERENCES |
| [$allElementsTrue](operators/allElementsTrue.md) | Sets | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$and](operators/and.md) | Logic | Yes | Yes | MONGO_6_SUBSET |
| [$anyElementTrue](operators/anyElementTrue.md) | Sets | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$arrayElemAt](operators/arrayElemAt.md) | Arrays | Yes | Yes | MONGO_6_DIFFERENCES |
| [$arrayToObject](operators/arrayToObject.md) | Arrays | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$asin](operators/asin.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$asinh](operators/asinh.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$atan](operators/atan.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$atan2](operators/atan2.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$atanh](operators/atanh.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$avg](operators/avg.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$binarySize](operators/binarySize.md) | Types and conversion | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$bitAnd](operators/bitAnd.md) | Arithmetic | No | Not in this docs suite | NON_MONGO_6_EXPRESSION |
| [$bitOr](operators/bitOr.md) | Arithmetic | No | Not in this docs suite | NON_MONGO_6_EXPRESSION |
| [$bitXor](operators/bitXor.md) | Arithmetic | No | Not in this docs suite | NON_MONGO_6_EXPRESSION |
| [$bsonSize](operators/bsonSize.md) | Types and conversion | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$ceil](operators/ceil.md) | Arithmetic | Yes | Yes | MONGO_6_DIFFERENCES |
| [$cmp](operators/cmp.md) | Comparison | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$coalesce](operators/coalesce.md) | Conditional | No | Not in this docs suite | NON_MONGO_6_EXPRESSION |
| [$concat](operators/concat.md) | Text | Yes | Yes | MONGO_6_DIFFERENCES |
| [$concatArrays](operators/concatArrays.md) | Arrays | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$cond](operators/cond.md) | Conditional | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$convert](operators/convert.md) | Types and conversion | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$cos](operators/cos.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$cosh](operators/cosh.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$dateAdd](operators/dateAdd.md) | Dates | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$dateDiff](operators/dateDiff.md) | Dates | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$dateFromParts](operators/dateFromParts.md) | Dates | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$dateFromString](operators/dateFromString.md) | Dates | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$dateSubtract](operators/dateSubtract.md) | Dates | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$dateToParts](operators/dateToParts.md) | Dates | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$dateToString](operators/dateToString.md) | Dates | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$dateTrunc](operators/dateTrunc.md) | Dates | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$dayOfMonth](operators/dayOfMonth.md) | Dates | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$dayOfWeek](operators/dayOfWeek.md) | Dates | No | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$dayOfYear](operators/dayOfYear.md) | Dates | No | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$degreesToRadians](operators/degreesToRadians.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$divide](operators/divide.md) | Arithmetic | Yes | Yes | MONGO_6_DIFFERENCES |
| [$endsWith](operators/endsWith.md) | Text | No | Not in this docs suite | NON_MONGO_6_EXPRESSION |
| [$eq](operators/eq.md) | Comparison | Yes | Yes | MONGO_6_SUBSET |
| [$exp](operators/exp.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$expr](operators/expr.md) | Advanced | No | Not in this docs suite | NON_MONGO_6_EXPRESSION |
| [$filter](operators/filter.md) | Arrays | No | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$first](operators/first.md) | Arrays | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$floor](operators/floor.md) | Arithmetic | Yes | Yes | MONGO_6_DIFFERENCES |
| [$function](operators/function.md) | Advanced | No | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$getField](operators/getField.md) | Objects | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$gt](operators/gt.md) | Comparison | Yes | Yes | MONGO_6_SUBSET |
| [$gte](operators/gte.md) | Comparison | Yes | Yes | MONGO_6_SUBSET |
| [$hour](operators/hour.md) | Dates | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$ifNull](operators/ifNull.md) | Conditional | Yes | Yes | MONGO_6_SUBSET |
| [$in](operators/in.md) | Comparison | Yes | Yes | MONGO_6_SUBSET |
| [$indexOfArray](operators/indexOfArray.md) | Arrays | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$indexOfBytes](operators/indexOfBytes.md) | Text | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$indexOfCP](operators/indexOfCP.md) | Text | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$isArray](operators/isArray.md) | Arrays | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$isNumber](operators/isNumber.md) | Types and conversion | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$isoDayOfWeek](operators/isoDayOfWeek.md) | Dates | No | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$isoWeek](operators/isoWeek.md) | Dates | No | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$isoWeekYear](operators/isoWeekYear.md) | Dates | No | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$last](operators/last.md) | Arrays | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$let](operators/let.md) | Conditional | No | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$literal](operators/literal.md) | Types and conversion | No | Not in this docs suite | MONGO_6_SUBSET |
| [$ln](operators/ln.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$log](operators/log.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$log10](operators/log10.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$lt](operators/lt.md) | Comparison | Yes | Yes | MONGO_6_SUBSET |
| [$lte](operators/lte.md) | Comparison | Yes | Yes | MONGO_6_SUBSET |
| [$ltrim](operators/ltrim.md) | Text | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$map](operators/map.md) | Arrays | No | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$max](operators/max.md) | Arrays | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$mergeObjects](operators/mergeObjects.md) | Objects | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$millisecond](operators/millisecond.md) | Dates | No | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$min](operators/min.md) | Arrays | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$minDistance](operators/minDistance.md) | Arithmetic | No | Not in this docs suite | NON_MONGO_6_EXPRESSION |
| [$minute](operators/minute.md) | Dates | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$mod](operators/mod.md) | Arithmetic | Yes | Yes | MONGO_6_DIFFERENCES |
| [$month](operators/month.md) | Dates | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$multiply](operators/multiply.md) | Arithmetic | Yes | Yes | MONGO_6_DIFFERENCES |
| [$ne](operators/ne.md) | Comparison | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$nin](operators/nin.md) | Comparison | No | Not in this docs suite | NON_MONGO_6_EXPRESSION |
| [$nor](operators/nor.md) | Logic | No | Not in this docs suite | NON_MONGO_6_EXPRESSION |
| [$not](operators/not.md) | Logic | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$objectToArray](operators/objectToArray.md) | Arrays | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$or](operators/or.md) | Logic | Yes | Yes | MONGO_6_SUBSET |
| [$pow](operators/pow.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$radiansToDegrees](operators/radiansToDegrees.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$range](operators/range.md) | Arrays | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$reduce](operators/reduce.md) | Arrays | No | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$regexFind](operators/regexFind.md) | Text | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$regexFindAll](operators/regexFindAll.md) | Text | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$regexMatch](operators/regexMatch.md) | Text | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$replaceAll](operators/replaceAll.md) | Text | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$replaceOne](operators/replaceOne.md) | Text | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$reverseArray](operators/reverseArray.md) | Arrays | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$round](operators/round.md) | Arithmetic | Yes | Yes | MONGO_6_SUBSET |
| [$rtrim](operators/rtrim.md) | Text | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$second](operators/second.md) | Dates | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$setDifference](operators/setDifference.md) | Sets | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$setEquals](operators/setEquals.md) | Sets | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$setField](operators/setField.md) | Objects | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$setIntersection](operators/setIntersection.md) | Sets | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$setIsSubset](operators/setIsSubset.md) | Sets | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$setIsSuperset](operators/setIsSuperset.md) | Sets | No | Not in this docs suite | NON_MONGO_6_EXPRESSION |
| [$setUnion](operators/setUnion.md) | Sets | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$sin](operators/sin.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$sinh](operators/sinh.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$size](operators/size.md) | Arrays | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$slice](operators/slice.md) | Arrays | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$split](operators/split.md) | Text | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$sqrt](operators/sqrt.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$startsWith](operators/startsWith.md) | Text | No | Not in this docs suite | NON_MONGO_6_EXPRESSION |
| [$strLenBytes](operators/strLenBytes.md) | Text | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$strLenCP](operators/strLenCP.md) | Text | Yes | Yes | MONGO_6_SUBSET |
| [$strcasecmp](operators/strcasecmp.md) | Text | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$substr](operators/substr.md) | Text | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$substrBytes](operators/substrBytes.md) | Text | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$substrCP](operators/substrCP.md) | Text | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$subtract](operators/subtract.md) | Arithmetic | Yes | Yes | MONGO_6_DIFFERENCES |
| [$sum](operators/sum.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$switch](operators/switch.md) | Conditional | No | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$tan](operators/tan.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$tanh](operators/tanh.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$toBool](operators/toBool.md) | Types and conversion | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$toDate](operators/toDate.md) | Types and conversion | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$toDecimal](operators/toDecimal.md) | Types and conversion | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$toDouble](operators/toDouble.md) | Types and conversion | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$toInt](operators/toInt.md) | Types and conversion | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$toLong](operators/toLong.md) | Types and conversion | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$toLower](operators/toLower.md) | Text | Yes | Yes | MONGO_6_SUBSET |
| [$toObjectId](operators/toObjectId.md) | Types and conversion | No | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$toString](operators/toString.md) | Types and conversion | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$toUpper](operators/toUpper.md) | Text | Yes | Yes | MONGO_6_SUBSET |
| [$trim](operators/trim.md) | Text | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$trunc](operators/trunc.md) | Arithmetic | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$tsIncrement](operators/tsIncrement.md) | Dates | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$tsSecond](operators/tsSecond.md) | Dates | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$type](operators/type.md) | Types and conversion | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$unsetField](operators/unsetField.md) | Objects | Yes | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$week](operators/week.md) | Dates | No | Not in this docs suite | MONGO_6_DIFFERENCES |
| [$year](operators/year.md) | Dates | Yes | Not in this docs suite | MONGO_6_SUBSET |
| [$zip](operators/zip.md) | Arrays | No | Not in this docs suite | MONGO_6_DIFFERENCES |
