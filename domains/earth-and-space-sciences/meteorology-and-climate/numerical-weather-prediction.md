---
id: numerical-weather-prediction
title: Numerical Weather Prediction and Ensemble Forecasting
domain: earth-and-space-sciences
course: meteorology-and-climate
prerequisites:
- id: weather-map-analysis
  type: hard
- id: hydrostatic-balance-pressure-profile
  type: soft
- id: geostrophic-wind-and-balance
  type: soft
- id: scale-analysis-atmospheric-equations
  type: soft
- id: weather-forecasting-basics
  type: soft
- id: chaos-definition-and-properties
  type: soft
builds-toward: []
tags:
- weather-forecasting
- nwp
- data-assimilation
- ensemble-forecast
- chaos
- parameterization
stage: formal-systems
status: validated
---

# Numerical Weather Prediction and Ensemble Forecasting

## Core Idea
Numerical weather prediction (NWP) forecasts the weather by solving the physical equations of the atmosphere on a computer, starting from the best estimate of its present state. The work has three main steps: combine observations into a starting picture (data assimilation), step the equations forward in time on a grid, and turn the raw output into forecasts people can use. Because the atmosphere is chaotic, small errors in the starting state grow, which limits useful day-to-day forecasts to roughly two weeks. Ensemble forecasts run the model many times from slightly different starting states to show how certain a forecast is.

## How It's Best Learned
Treat the forecast as an initial-value problem: if you know the state now and the laws of change, you can step forward. Have students step a simple equation forward by hand for a few time steps to feel how time steps and grid spacing work. Then show an ensemble "spaghetti plot" of one contour line from many runs, and discuss why the lines spread apart with forecast lead time.

## Common Misconceptions
- A computer forecast is just a search for past weather that looked like today. (Modern NWP solves the equations of motion, thermodynamics, and moisture; matching past patterns is a much older and weaker method.)
- If forecasts were perfect, models could predict daily weather a season ahead. (Chaos makes small errors grow, so even a perfect model with near-perfect data loses day-to-day skill after about two weeks.)
- A 40 percent chance of rain means it will rain over 40 percent of the area. (It is the probability that measurable rain falls at a given point during the forecast period.)
- Models simulate every cloud and gust. (Processes smaller than the grid spacing, such as most individual clouds and turbulence, are represented by approximate rules called parameterizations.)

## Questions

```yaml
- question: "What is the purpose of data assimilation in numerical weather prediction?"
  type: multiple-choice
  options:
    - "To average the outputs of different forecast models"
    - "To combine new observations with a short-range model forecast to produce the best estimate of the current state, which then starts the next forecast"
    - "To remove chaotic behavior from the equations"
    - "To convert model output into television graphics"
  answer: 1
  explanation: "Observations are scattered and imperfect, and the model needs a value at every grid point. Data assimilation blends observations with a recent short-range forecast, weighting each by its expected error, to build the starting state called the analysis."

- question: "Why do ensemble forecasts start each run from a slightly different initial state?"
  type: short-answer
  answer: "The true initial state is never known exactly, and in a chaotic atmosphere small differences grow over time. Starting many runs from slightly different but plausible states samples this uncertainty. If the runs stay close together the forecast is more reliable; if they spread apart, confidence is lower."
  explanation: "The spread of the ensemble is a forecast of the forecast's own uncertainty. This is the practical answer to the predictability limit that Edward Lorenz identified in the 1960s."

- question: "A model with a grid spacing of 10 km can directly resolve individual thunderstorm updrafts that are about 1 km wide."
  type: true-false
  answer: false
  explanation: "A feature must span several grid points to be represented well. A 1 km updraft is far smaller than a 10 km grid box, so its effects must be estimated with a convection parameterization."

- question: "Lewis Fry Richardson's hand-calculated forecast, published in 1922, predicted a surface pressure change of about 145 hPa in six hours. What was the main lesson for later forecasters?"
  type: multiple-choice
  options:
    - "The equations of the atmosphere are wrong"
    - "Weather cannot be forecast by calculation"
    - "The method was sound, but unbalanced initial data and numerical problems can wreck a forecast, so the starting state and numerical methods need careful treatment"
    - "Only computers can solve the equations of motion"
  answer: 2
  explanation: "Richardson's approach is the basis of modern NWP. His huge error came mainly from imbalances in the initial data, which produced unrealistic fast waves. Later work on balanced initial states, stable numerical methods, and fast computers made his idea practical."
```

## Explainer
At the start of the twentieth century, the Norwegian scientist Vilhelm Bjerknes argued that forecasting could be treated as a physics problem. If you know the state of the atmosphere now and the laws that govern it, you can calculate its future. Those laws include Newton's second law for moving air, conservation of mass, the first law of thermodynamics, and the gas law, along with equations for water vapor.

Lewis Fry Richardson tried this by hand during the First World War and published the result in 1922. It took him weeks to compute a six-hour forecast, and the answer was badly wrong. The idea worked once computers arrived. In 1950, Jule Charney, Ragnar Fjørtoft, and John von Neumann ran the first computer forecast on the ENIAC, using a simplified equation for the flow at mid-levels.

A modern forecast cycle has three parts. First comes **data assimilation**. Millions of observations from weather balloons, satellites, aircraft, ships, and surface stations are blended with a short-range forecast to estimate the state of the atmosphere at every grid point. Second comes the **model run**. The globe is divided into a three-dimensional grid, and the equations are stepped forward in short time steps. Processes smaller than a grid box, such as most clouds, turbulence, and radiation in detail, are handled by **parameterizations**. Third comes **post-processing**, which corrects known model biases and turns the output into temperature, wind, and precipitation forecasts.

There is a limit to how far ahead this can work. In 1963, Edward Lorenz showed that a simple model of convection was extremely sensitive to its starting values. Tiny differences grew until two runs looked nothing alike. The real atmosphere behaves the same way. Even with an excellent model, day-to-day forecasts lose their skill after about two weeks.

Forecasters respond with **ensembles**. Instead of one run, a center runs dozens, each starting from a slightly different but realistic state. When the members agree, confidence is high. When they spread apart, the forecast is uncertain, and the ensemble can give probabilities, such as a 70 percent chance of more than 10 mm of rain. Better observations, better assimilation, and faster computers have steadily lengthened the range of useful forecasts.
