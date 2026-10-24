# Condition recipes

These are SrotaX condition recipes from the API catalog. Some combine multiple engine operators; recipe names must not be presented as MongoDB operators.

## Comparison

| Label | Recipe | Input types | Operand kind | Engine dependencies |
| --- | --- | --- | --- | --- |
| Equals | `$eq` | number, string, boolean, date, array, object | scalar | $cond, $eq, $isNumber, $literal, $toDate, $type |
| Does not equal | `$ne` | number, string, boolean, date, array, object | scalar | $cond, $eq, $isNumber, $literal, $ne, $toDate, $type |
| Greater than | `$gt` | number, string, date | scalar | $cond, $eq, $gt, $isNumber, $literal, $toDate, $type |
| Greater than or equal to | `$gte` | number, string, date | scalar | $cond, $eq, $gte, $isNumber, $literal, $toDate, $type |
| Less than | `$lt` | number, string, date | scalar | $cond, $eq, $isNumber, $literal, $lt, $toDate, $type |
| Less than or equal to | `$lte` | number, string, date | scalar | $cond, $eq, $isNumber, $literal, $lte, $toDate, $type |

## Membership

| Label | Recipe | Input types | Operand kind | Engine dependencies |
| --- | --- | --- | --- | --- |
| Is one of | `$in` | number, string, boolean, date, array, object | list | $cond, $eq, $in, $isNumber, $literal, $toDate, $type |
| Is not one of | `$nin` | number, string, boolean, date, array, object | list | $cond, $eq, $in, $isNumber, $literal, $not, $toDate, $type |

## Text

| Label | Recipe | Input types | Operand kind | Engine dependencies |
| --- | --- | --- | --- | --- |
| Contains | `$contains` | string | scalar | $cond, $eq, $gte, $indexOfCP, $literal, $type |
| Does not contain | `$notContains` | string | scalar | $cond, $eq, $gte, $indexOfCP, $literal, $not, $type |
| Starts with | `$startsWith` | string | scalar | $cond, $eq, $literal, $regexMatch, $type |
| Ends with | `$endsWith` | string | scalar | $cond, $eq, $literal, $regexMatch, $type |
| Matches pattern | `$regexMatch` | string | scalar | $cond, $eq, $literal, $regexMatch, $type |
| Equals ignoring case | `$equalsIgnoreCase` | string | scalar | $cond, $eq, $literal, $toLower, $type |
| Is blank | `$isBlank` | string | none | $cond, $eq, $trim, $type |
| Is not blank | `$isNotBlank` | string | none | $cond, $eq, $ne, $trim, $type |

## Presence

| Label | Recipe | Input types | Operand kind | Engine dependencies |
| --- | --- | --- | --- | --- |
| Exists | `$exists` | number, string, boolean, date, array, object | none | $ne, $type |
| Is missing | `$isMissing` | number, string, boolean, date, array, object | none | $eq, $type |
| Is null | `$isNull` | number, string, boolean, date, array, object | none | $eq, $type |
| Is not null | `$isNotNull` | number, string, boolean, date, array, object | none | $in, $not, $type |

## Empty values

| Label | Recipe | Input types | Operand kind | Engine dependencies |
| --- | --- | --- | --- | --- |
| Is empty | `$isEmpty` | string, array | none | $cond, $eq, $size, $type |
| Is not empty | `$isNotEmpty` | string, array | none | $cond, $eq, $ne, $size, $type |

## Lists

| Label | Recipe | Input types | Operand kind | Engine dependencies |
| --- | --- | --- | --- | --- |
| Contains a value | `$containsValue` | array | json | $cond, $eq, $in, $literal, $type |
| Contains all | `$containsAll` | array | list | $cond, $eq, $literal, $setIsSubset, $type |
| Contains any | `$containsAny` | array | list | $cond, $eq, $gt, $literal, $setIntersection, $size, $type |
| Contains none | `$containsNone` | array | list | $cond, $eq, $literal, $setIntersection, $size, $type |
| Has the same values | `$setEquals` | array | list | $cond, $eq, $literal, $setEquals, $type |
| Is a subset of | `$setIsSubset` | array | list | $cond, $eq, $literal, $setIsSubset, $type |

## Range

| Label | Recipe | Input types | Operand kind | Engine dependencies |
| --- | --- | --- | --- | --- |
| Between | `$between` | number, date | range | $and, $cond, $eq, $gte, $isNumber, $literal, $lte, $toDate, $type |
| Not between | `$notBetween` | number, date | range | $and, $cond, $eq, $gte, $isNumber, $literal, $lte, $not, $toDate, $type |

## Length

| Label | Recipe | Input types | Operand kind | Engine dependencies |
| --- | --- | --- | --- | --- |
| Length equals | `$lengthEq` | string, array | number | $cond, $eq, $literal, $size, $strLenCP, $type |
| Length greater than | `$lengthGt` | string, array | number | $cond, $eq, $gt, $literal, $size, $strLenCP, $type |
| Length less than | `$lengthLt` | string, array | number | $cond, $eq, $literal, $lt, $size, $strLenCP, $type |

## Dates

| Label | Recipe | Input types | Operand kind | Engine dependencies |
| --- | --- | --- | --- | --- |
| Same calendar day (UTC) | `$sameDay` | date | scalar | $cond, $dateToString, $eq, $literal, $toDate, $type |
| Different calendar day (UTC) | `$differentDay` | date | scalar | $cond, $dateToString, $eq, $literal, $ne, $toDate, $type |

## Boolean

| Label | Recipe | Input types | Operand kind | Engine dependencies |
| --- | --- | --- | --- | --- |
| Is true | `$isTrue` | boolean | none | $eq |
| Is false | `$isFalse` | boolean | none | $eq |

## Aggregate List operations

| Operation | Requires a field |
| --- | --- |
| Count items (`count`) | False |
| Sum (`sum`) | True |
| Average (`average`) | True |
| Minimum (`min`) | True |
| Maximum (`max`) | True |
