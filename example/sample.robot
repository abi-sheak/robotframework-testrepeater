*** Test Cases ***
Addition of Two numbers
    [Tags]  add
	${OUTPUT}  Evaluate    1 + 2
	Log    ${OUTPUT}

Substraction of two numbers
    [Tags]  sub
    ${OUTPUT}  Evaluate    1 - 2
	Log    ${OUTPUT}

Multiplication of two numbers
    [Tags]  mul
    ${OUTPUT}  Evaluate    1 * 2
	Log    ${OUTPUT}

Division of two numbers
    [Tags]  div
    ${OUTPUT}  Evaluate    1 / 2
	Log    ${OUTPUT}
