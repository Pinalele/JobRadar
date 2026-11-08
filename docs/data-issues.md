1. Título: clean_title breaks apostrophes

markdown
## Problem
`clean_title` capitalises the letter after an apostrophe.

## Example
"Women's Business Center" becomes "Women'S Business Center".

## Expected
"Women's Business Center"

## Labels
bug

2. Título: Company names have extra spaces or wrong capitalisation

markdown
## Problem
Company names are printed exactly as they come from the CSV.

## Examples
- "The National Exemplar " (trailing space)
- "CLEVELAND KIDS BOOK BANK" (all capitals)

## Expected
Company names are trimmed. Capitalisation is left as-is for now, since some companies use capitals on purpose (e.g. "PGAV Destinations").

## Labels
data-quality

3. Título: Some postings have no company name

markdown
## Problem
Some rows have an empty `company_name`, which prints as "@  (City)".

## Expected
Show "Unknown company" when the name is missing.

## Labels
data-quality

4. Título: Location is not always a city

markdown
## Problem
`get_city` assumes "City, Region", but some locations are a country or a region.

## Examples
- "United States"
- "Greater Philadelphia"

## Expected
Locations without a comma are kept as they are, and a country-only location such as "United States" is shown as "Remote / unspecified".

## Labels
data-quality

5. Título: Many postings have no salary

markdown
## Problem
11 of the first 20 postings have no `max_salary`.

## Expected
- Keep showing "salary not available" (already handled).
- Count how many postings in the whole file have a salary.

## Labels
data-quality, analysis

6. Título: Some salaries look suspicious

markdown
## Problem
Some salaries look too high or too low for the role and could distort averages.

## Example
Producer at 300,000.00 per year.

## Expected
Investigate later: define a reasonable range and flag values outside it.

## Labels
data-quality, later

7. Título: Some titles are not job roles

markdown
## Problem
Some `title` values are organisation names instead of job roles.

## Example
"Appalachian Highlands Women's Business Center"

## Expected
Investigate later. Filtering AI roles (week 2) will remove most of these.

## Labels
data-quality, later

8. Título: Filter postings to AI roles only

markdown
## Problem
The dataset covers all industries; none of the first 20 postings are AI roles.

## Expected
Keep only postings whose title contains AI-related keywords (AI, ML, Machine Learning, LLM). Planned for week 2.

## Labels
feature