# Tutorial 2

## Scenario
 The admission policy for the movie theater
 - Users are 13 years old or older, OR
 - Users are accompanied by an adult, AND
 - User must have a valid ticket

 # Activity 

 ## Components 

 - 1.1. Here the inputs are Age , accompanied by an adult and must have a valid ticket. 

 - 1.2. Here the process is to check if the user >= 13 || accomapanied by adult = TRUE && valid ticket = TRUE

 - 1.3. Here the output is suppossed to be 'Admission accepted' or 'Admission Denied' 

 ## Algorithm 

 - 2.1. Diagram 
 ![alt text](image.png)

 - 2.2. TRUTH TABLE 

 | Age >= 13 | Adult Present | Valid Ticket | Admission |
|------------|--------------|--------------|------------|
| F | F | F | Denied |
| F | F | T | Denied |
| F | T | F | Denied |
| F | T | T | Allowed |
| T | F | F | Denied |
| T | F | T | Allowed |
| T | T | F | Denied |
| T | T | T | Allowed |

- 2.3. ALGORITHM 

1. Start
2. Input age
3. Input accompanied by adult
4. Input valid ticket
5. If (age >= 13 || accompanied by adult) && valid ticket
   - Display "Admission Allowed"
6. Else
   - Display "Admission Denied"
7. End

- 2.4. PSEUDOCODE 

INPUT age

INPUT accompaniedByAdult

INPUT validTicket

IF (age >= 13 || accompaniedByAdult = TRUE) && validTicket = TRUE THEN

    DISPLAY "Admission Allowed"

ELSE

    DISPLAY "Admission Denied"

END

# EVALUATION OF EXPRESSION 
## Sample inputs 

| Age | Adult Present | Valid Ticket | Result |
|------|--------------|--------------|--------|
| 15 | No | Yes | Allowed |
| 10 | Yes | Yes | Allowed |
| 10 | No | Yes | Denied |
| 16 | No | No | Denied |