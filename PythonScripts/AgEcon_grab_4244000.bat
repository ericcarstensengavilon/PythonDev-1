echo off
rem FOR /L %%y IN (15, 1, 25) DO ECHO %%y
rem PAUSE

SET YEAR=%DATE:~-4%
SET /a ENDYEAR=%year% - 1
REM ECHO %ENDYEAR%

rem 0111000 0113000 0114200 0114300 0224200 0230000 0240000 0410000 0422110 0430000 0440000 0451000 0452000 0459100 0459200 0459900 0612000 
rem 0813100 0813101 0813200 0813300 0813500 0813600 0813700 0813800 0814200 2221000 2222000 2222001 2223000 2224000 2226000 2231000 2232000 4232000 
rem 4232001 4233000 4234000 4235000 4236000 4239100 4242000 4243000 4244000)

ECHO OFF
FOR %%x IN (4244000) DO (
	FOR /L %%y IN (1990, 1, 2021) DO (
		ECHO %%x %%y
		call \\tepfil01\BatchPRD\AgEcon\PSD_Data\USDA_FAS_WebApi.exe %%x %%y))
	
GOTO END

::Legend
Barley
0430000 

Corn
0440000 

Millet
0459100 

Mixed Grain
0459900 

Oats
0452000 

Rye
0451000 

Sorghum
0459200 

Wheat 
0410000 

Rice, Milled 
0422110 

Wheat
0410000 

Sugar, Centrifugal  
0612000 

Dairy, Butter 
0230000 

Dairy, Cheese 
0240000 

Dairy, Milk, Nonfat Dry
0224200 

Meal, Copra 
0813700 

Meal, Cottonseed 
0813300 

Meal, Fish 
0814200 

Meal, Palm Kernel 
0813800 

Meal, Peanut 
0813200 

Meal, Rapeseed 
0813600 

Meal, Soybean 
0813100 

Meal, Soybean (Local) 
0813101 

Meal, Sunflowerseed 
0813500 

Meat, Beef and Veal 
0111000 

Meat, Swine 
0113000 

Oil, Coconut 
4242000 

Oil, Cottonseed 
4233000 

Oil, Olive 
4235000 

Oil, Palm 
4243000 

Oil, Palm Kernel 
4244000 

Oil, Peanut 
4234000 

Oil, Rapeseed 
4239100 

Oil, Soybean 
4232000 

Oil, Soybean (Local) 
4232001 

Oil, Sunflowerseed 
4236000 

Oilseed, Copra 
2231000 

Oilseed, Cottonseed 
2223000 

Oilseed, Palm Kernel 
2232000 

Oilseed, Peanut 
2221000 

Oilseed, Rapeseed 
2226000 

Oilseed, Soybean 
2222000 

Oilseed, Soybean (Local) 
2222001 

Oilseed, Sunflowerseed 
2224000 

Poultry, Meat, Broiler 
0114200 

Poultry, Meat, Turkey 
0114300 

:END
