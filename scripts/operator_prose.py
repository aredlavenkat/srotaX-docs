"""Reader-facing argument descriptions; catalog enum labels never become API values."""
DESCRIPTIONS = {
 'input':'Expression supplying the value to process. A field reference such as `"$price"` reads from the current document.',
 'value':'Expression supplying the value to evaluate.', 'number':'Numeric expression. Repeat the argument when the syntax accepts multiple operands.',
 'integer':'Integer expression used in the bitwise operation.', 'expression':'Expression to evaluate as a condition.',
 'array':'Expression supplying the source array.', 'other':'Expression supplying the other array for the set operation.',
 'object':'Expression supplying an object to combine.', 'text':'Expression supplying the text value.',
 'left':'First expression in the ordered argument list.', 'right':'Second expression in the ordered argument list.',
 'index':'Zero-based array position. A negative position counts from the end.',
 'if':'Condition expression that selects the result branch.', 'then':'Result expression selected when the condition is true.',
 'else':'Result expression selected when the condition is false.',
 'to':'Target type name or numeric type code. See Supported values below; for example, `"int"` or `16`.',
 'onError':'Fallback expression for a supported conversion/parsing failure. If omitted, that failure raises an error.',
 'onNull':'Fallback expression for null or missing input. If omitted, the null-input result is null.',
 'startDate':'Expression supplying the starting date.', 'endDate':'Expression supplying the ending date.',
 'date':'Expression supplying the date to process.', 'dateString':'Expression supplying a date string to parse.',
 'unit':'Time unit name, such as `"day"` or `"hour"`. See Supported values below.',
 'amount':'Number of time units to add or subtract.',
 'timezone':'Timezone name or offset used for the calendar operation, for example `"America/Toronto"` or `"+05:30"`.',
 'startOfWeek':'Weekday name for week-based calculations, for example `"monday"`.',
 'binSize':'Number of units in each truncation interval.',
 'format':'Date format string. See Supported values below for the tokens implemented by this operator.',
 'year':'Calendar year expression.', 'month':'Calendar month expression.', 'day':'Day-of-month expression.',
 'hour':'Hour expression.', 'minute':'Minute expression.', 'second':'Second expression.', 'millisecond':'Millisecond expression.',
 'isoWeekYear':'ISO week-numbering year. Use the ISO fields instead of the calendar year/month/day fields.',
 'isoWeek':'ISO week number.', 'isoDayOfWeek':'ISO weekday number.', 'iso8601':'Boolean selecting ISO week-based output fields.',
 'as':'Literal variable name for the current array item; defaults to `"this"`. Refer to it as `$$name` in the nested expression.',
 'cond':'Condition evaluated for each array item. Items with a matching condition are retained.',
 'n':'Positive integer count of elements to return.',
 'body':'Literal function body understood by the engine function implementation.',
 'args':'Array of expressions passed as function arguments.', 'lang':'Literal function-language selector.',
 'field':'Expression supplying the field name to read or change.',
 'fallback':'Expression to use when the preceding input is null or missing.',
 'search':'Value or substring to find in the source.',
 'start':'Starting position or lower bound. See the syntax and examples for this operator.',
 'end':'Exclusive ending position or upper bound.',
 'vars':'Object mapping variable names to expressions. Reference each variable as `$$name` inside `in`.',
 'in':'Expression evaluated within the operator’s variable scope.',
 'chars':'Characters to remove from the ends of the string. If omitted, the operator uses its whitespace trimming behavior.',
 'method':'Literal `"approximate"`. Other method names are rejected.',
 'p':'Array of requested percentiles, each between `0` and `1` inclusive.',
 'points':'Expression supplying the candidate points.', 'spherical':'Boolean selecting spherical distance calculation.',
 'step':'Increment between generated values. Defaults to `1`; use a negative step for descending values.',
 'initialValue':'Starting accumulator value. Inside `in`, use `$$value` for the accumulator and `$$this` for the current item.',
 'regex':'Regular-expression pattern to search for.',
 'options':'Regex option string. See Supported values below.',
 'find':'Substring to replace.', 'replacement':'Replacement text.',
 'place':'Decimal position for rounding or truncation. Defaults to `0`; negative positions act to the left of the decimal point.',
 'positionOrCount':'With two arguments, the number of elements to keep. With three arguments, the starting position.',
 'count':'Number of elements to keep in the three-argument form.',
 'sortBy':'Literal `1` for ascending or `-1` for descending; for object items, an ordered object of field names and directions.',
 'delimiter':'String separating the output parts.', 'length':'Number of bytes or characters to return, depending on the operator.',
 'branches':'Array of objects containing `case` and `then` expressions, evaluated in order.',
 'default':'Result expression used when no branch matches. The current engine returns null when this is omitted.',
 'inputs':'Array of expressions, each resolving to an array to combine by position.',
 'useLongestLength':'Literal boolean. Defaults to `false` (shortest input); `true` uses the longest input and pads shorter inputs.',
}
OVERRIDES={
 ('$divide','left'):'Dividend expression.',('$divide','right'):'Divisor expression.',
 ('$subtract','left'):'Expression to subtract from.',('$subtract','right'):'Expression to subtract.',
 ('$pow','left'):'Base expression.',('$pow','right'):'Exponent expression.',
 ('$log','left'):'Number whose logarithm is calculated.',('$log','right'):'Logarithm base.',
 ('$atan2','left'):'Y-coordinate expression.',('$atan2','right'):'X-coordinate expression.',
 ('$mod','left'):'Dividend expression.',('$mod','right'):'Divisor expression.',
 ('$range','start'):'Inclusive starting integer.',('$range','end'):'Exclusive ending integer.',
 ('$map','in'):'Expression evaluated for each item using `$$this` or the variable named by `as`.',
 ('$reduce','in'):'Expression evaluated for each item with `$$this` (item) and `$$value` (accumulator).',
 ('$literal','input'):'Value to return without evaluating field paths or nested operators.',
 ('$toArray','input'):'String containing a JSON array. Existing array values are rejected; this operator parses strings.',
 ('$toObject','input'):'String containing a JSON object. Existing object values are rejected; this operator parses strings.',
}
def parameter_description(op,arg):
 description=OVERRIDES.get((op,arg['name']),DESCRIPTIONS[arg['name']])
 name=arg['name']
 if name=='timezone':description+=' Defaults to UTC when omitted.'
 if op=='$dateFromParts' and name in ['month','day','isoWeek','isoDayOfWeek']:description+=' Defaults to 1.'
 if op=='$dateFromParts' and name in ['hour','minute','second','millisecond']:description+=' Defaults to 0.'
 if op=='$dateFromParts' and name in ['year','isoWeekYear']:description+=' Valid years are 1 through 9999.'
 if name=='iso8601':description+=' Defaults to false.'
 if name=='binSize':description+=' Defaults to 1.'
 if op=='$dateToString' and name=='format':description+=' Default: `%Y-%m-%dT%H:%M:%S.%LZ` for UTC, or `%Y-%m-%dT%H:%M:%S.%L` for a non-UTC zone.'
 if op=='$minDistance' and name=='spherical':description='Literal boolean, default false. True returns great-circle distance in meters; false returns Euclidean distance in coordinate units.'
 if op=='$minDistance' and name=='input':description='Origin point as `[longitude, latitude]` or an object with a `coordinates` array.'
 if op=='$minDistance' and name=='points':description='Array of candidate points in the same format as input.'
 return description

def syntax(d):
 op=d['name'];args=d['operands'];kind=d['argumentSyntax']
 if kind=='SINGLE':return '{ "'+op+'": <expression> }'
 if kind=='POSITIONAL':
  parts=['<'+a['name']+'>' for a in args]
  if d['maxArguments']<0:parts.append('...')
  return '{ "'+op+'": [ '+', '.join(parts)+' ] }'
 return '{\n  "'+op+'": {\n'+',\n'.join('    "'+a['name']+'": <'+a['name']+'>' for a in args)+'\n  }\n}'
