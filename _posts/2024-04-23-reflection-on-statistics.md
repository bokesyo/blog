---
layout: post
title:  Reflections on Statistics
date:   2024-04-23 00:40:16
description: 
tags: thoughts
categories: thoughts
published: true
---

Today, while working on a statistics assignment, I found an answer on Google for a question that has been around since 2004. It made me wonder why, despite many years of progress in statistics, no teacher ever told me:

1. The normal distribution can be described using only the first and second moments; third moments or higher are not needed. This means that the first and second moments are sufficient statistics for data that follows a normal distribution.

2. When we assume data follows a normal distribution, we can derive the distributions for any necessary metrics from the normal distribution itself. These metrics depend heavily on human intuition and can often be defined arbitrarily. Once a metric is defined, its distribution can likely be deduced, allowing for hypothesis testing.

3. All tools in linear regression rely on the assumption that residuals follow a normal distribution. If the residuals followed a Laplace distribution, these tools would not hold. But why must residuals follow a normal distribution? Perhaps it's because many unconsidered variables exist, and the average or linear combination of numerous variables results in a normal distribution. Including more variables can reduce the absolute value of residuals.

Is it possible that the founders of statistical inference valued these assumptions, but over years of tradition, they became less emphasized?
