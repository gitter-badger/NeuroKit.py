# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import plotly
import plotly.offline as py
import plotly.graph_objs as go
import scipy
import scipy.stats
import math



# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def correlation(var1, var2, data=None, r_type="pearson", plot=True, jitter_points=False, output=True):
    """
    Performs a correlation.

    Parameters
    ----------
    NA

    Returns
    ----------
    NA

    Example
    ----------
    NA

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - scipy
    """
    if data is not None:
        var1_name = var1
        var2_name = var2
        var1 = data[var1]
        var2 = data[var2]
    else:
        data = pd.DataFrame({"VARIABLE1":var1,"VARIABLE2":var2})
        var1 = data["VARIABLE1"]
        var2 = data["VARIABLE2"]
        var1_name = "VARIABLE1"
        var2_name = "VARIABLE2"


    result = {}

    if r_type == "spearman":
        result["Correlation_Type"] = "Spearman's"
        result["Correlation_Symbol"]= "Spearman's ρ"
        result["r"], result["p"] = scipy.stats.spearmanr(var1, var2)
        if plot is True:
            print("NEUROPSYDIA WARNING: correlation(): plot=True not available for spearman's correlation")

        if result["r"] < 0:
            result["Direction"] = "negative"
        else:
            result["Direction"] = "positive"
        if abs(result['r']) < 0.30:
            result['strength'] = 'weak'
        elif abs(result['r']) > 0.70:
            result['strength'] = 'strong'
        else:
            result['strength'] = 'moderate'

        result["APA_output"] = "A %s rank correlation coefficient was computed to assess the relationship between %s and %s. There was a %s %s correlation between the two variables (%s = %0.2f, n = %i, p = %.3f)." %(result["Correlation_Type"], var1_name, var2_name, result['strength'], result["direction"], result["Correlation_Symbol"], result["r"], len(var1), result["p"])


    else:
        result["Correlation_Type"] = "Pearson's"
        result["Correlation_Symbol"]= "r"
        slope, intercept, result["r"], result["p"], std_err = scipy.stats.linregress(var1, var2)

        z = np.arctanh(result["r"])
        cint = z + np.array([-1, 1]) * std_err * scipy.stats.norm.ppf((1+0.95)/2)
        result["CI"] = np.tanh(cint)
        result["description_var1"] = [np.mean(var1), np.std(var1), min(var1), max(var1)]
        result["description_var2"] = [np.mean(var2), np.std(var2), min(var2), max(var2)]



        if result["r"] < 0:
            result["direction"] = "negative"
            result["direction2"] = "decrease"
        else:
            result["direction"] = "positive"
            result["direction2"] = "increase"
        if abs(result['r']) < 0.30:
            result['strength'] = 'weak'
        elif abs(result['r']) > 0.70:
            result['strength'] = 'strong'
        else:
            result['strength'] = 'moderate'

        result["APA_output"] = "A %s correlation coefficient was computed to assess the linear relationship between %s and %s. There was a %s %s correlation between the two variables (%s = %0.2f (95%% CI [%0.2f, %0.2f]), n = %i, p = %.3f, R² = %.2f). An increase of 1 on %s (M = %.2f, SD = %.2f, min = %.2f, max = %.2f) lead to an %s of %0.2f on %s (M = %.2f, SD = %.2f, min = %.2f, max = %.2f)." %(result["Correlation_Type"], var1_name, var2_name, result['strength'], result["direction"], result["Correlation_Symbol"], result["r"], result["CI"][0], result["CI"][1], len(var1), result["p"], result["r"]**2, var1_name, result["description_var1"][0], result["description_var1"][1], result["description_var1"][2], result["description_var1"][3], result["direction2"], abs(slope), var2_name, result["description_var2"][0], result["description_var2"][1], result["description_var2"][2], result["description_var2"][3])



        if plot is True:

            line = slope*var1+intercept

            if jitter_points is True:
                jitter1 = np.random.random_sample(len(var1))
                jitter2 = np.random.random_sample(len(var2))
                jitter1 =  np.std(var1)/6 * jitter1
                jitter2 =  np.std(var2)/6 * jitter2
                x = np.array(var1)+jitter1
                y = np.array(var2)+jitter2
            else:
                x = var1
                y = var2
            trace1 = go.Scatter(
                      x=x,
                      y=y,
                      mode='markers',
                      marker=go.Marker(color='rgb(255, 127, 14)'),
                      name='Data points'
                      )

            trace2 = go.Scatter(
                              x=var1,
                              y=line,
                              mode='lines',
                              marker=go.Marker(color='rgb(31, 119, 180)'),
                              name='Regression line'
                              )
            layout = go.Layout(
                      xaxis=dict(
                        showgrid=True
                        ),
                      yaxis=dict(
                        showgrid=True
                        )
                    )
            plot = go.Figure(data=[trace1, trace2], layout=layout)
            py.plot(plot)

    if output is True:
        print(result["APA_output"])
    return(result)
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def select_variables(df, dtype="numeric"):
    """
    Keep a specific type subset of your pandas dataframe.

    Parameters
    ----------
    df = pandas.DataFrame object
        a pandas dataframe
    dtype = str, optional
        "numeric" or "factor". Note that right now, entering something else than "numeric" will just result in a dataframe with all non-numeric variables.

    Returns
    ----------
    subset = pandas.DataFrame object
        the subsetted dataframe

    Example
    ----------
    NA

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - pandas
    """
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    if dtype == "numeric":
        subset = df.copy().select_dtypes(include = numerics)
    else:
        subset = df.copy().select_dtypes(include != numerics)
    return(subset)


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def t_test(var1, var2, data=None, var1_name="VARIABLE-1", var2_name="VARIABLE-2", independent=False, output=True, plot=True, bayesian=False, bootstrapped=True, N_resamples=1000, significance_treshold=0.05):
    """
    Performs a t-test.

    Parameters
    ----------
    var1 = list/array
        a numeric variable
    var2 = list/array
        either a numeric variable or a factor (with 2 levels)
    var1_name = str
        name of the first variable
    var2_name = str
        name of the second variable
    independent = bool
        pairwise or two-sample. Is adjusted automatically depending on the type of var2.
    output = bool
        if True, print the summary using APA6 style
    plot = bool
        if True, open a html window with a distribution plot
    bayesian = bool
        feature not implemented yet
    bootstrapped = bool
        if False, do a "traditional" t-test (and assumes the usual stuff about normal distrubtion of the data). If True, do a boostrapped t-test (tries to get closer of the true distribution of the data)
    N_resamples = int
        the number of resamples in case of a bootstrapped t-test
    significance_treshold = float
        under what treshold should the difference be considered as significant

    Returns
    ----------
    dic
        a result dictionnary containing the different computed values.

    Example
    ----------
    >>> import numpy as np
    >>> import neurokit as nk
    >>> # generate variables
    >>> variable1 = np.random.normal(3, 1, 1000)  # get a normal distribution of size = 1000
    >>> variable2 = np.random.normal(2.5, 0.1.2, 1000)  # get a second normal distribution of size = 1000
    >>> factor = ["a","a","b","b"] * 250  # get a factor with a and b levels of size = 1000
    >>> # paired-samples t-test
    >>> nk.t_test(var1, var2)
    >>> # independent t-test
    >>> nk.t_test(var1, factor)

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - pandas
    - numpy
    - plotly
    - scipy
    - pymc3
    """
    if data is not None:
        var1 = data[var1]
        var2 = data[var2]
        var1_name = var1
        var2_name = var2

    var1 = list(var1)
    var2 = list(var2)

    assert len(var1) == len(var2), "NEUROPSYDIA ERROR: t_test(): variables are not of the same length."
    result = {}

    if len(set(var2)) == 2:
        independent = True
        factor1 = str(list(set(var2))[0])
        factor2 = str(list(set(var2))[1])
        var1_sorted = [x for (y,x) in sorted(zip(var2,var1))]
        var1 = var1_sorted[:var2.count(list(set(var2))[0])]
        var2 = var1_sorted[var2.count(list(set(var2))[0]):]
        result['dof'] = 1
    else:
        try:
            np.array(var2) + 3  # Check if numeric
            independent = False
        except TypeError:
            print("NEUROPSYDIA ERROR: t_test(): %s is not entirely made of numerics or contains more than 2 levels." %(var2_name))
            return()


    if independent != True:
        result['dof'] = len(var1)


    result['n1'] = len(var1)
    result['n2'] = len(var2)
    result['mean1'] = np.mean(var1)
    result['sd1'] = np.std(var1)
    result['mean2'] = np.mean(var2)
    result['sd2'] = np.std(var2)
    result['difference'] = result['mean1'] - result['mean2']

    result['d'] = abs(result['difference'] / ((result['sd1']**2 + result['sd2']**2)/2)**0.5)
    if result['d'] < 0.20:
        result['interpretation_d'] = "Following Cohen's (1988) recommandations, the effect size for this analysis could be characterized as small (d = %.2f, < 0.20)." %(result['d'])
    elif result['d'] < 0.50:
        result['interpretation_d'] = "Following Cohen's (1988) recommandations, the effect size for this analysis could be characterized as medium (d = %.2f, < 0.50)." %(result['d'])
    elif result['d'] < 0.80:
        result['interpretation_d'] = "Following Cohen's (1988) recommandations, the effect size for this analysis could be characterized as large (d = %.2f)." %(result['d'])
    else:
        result['interpretation_d'] = "Following Cohen's (1988) recommandations, the effect size for this analysis could be characterized as very large (d = %.2f)." %(result['d'])

    if plot is True:
        if independent is True:
            figure = plotly.tools.FigureFactory.create_distplot([var1, var2], group_labels=[factor1, factor2])
        else:
            figure = plotly.tools.FigureFactory.create_distplot([var1, var2], group_labels=[var1_name, var2_name])
        py.plot(figure)

    if bayesian is True:
#        from theano import config
#        config.warn.sum_div_dimshuffle_bug = False
#        import pymc3 as pm
        print("NEUROPSYDIA WARNING: t_test(): bayesian estimation not implemented yet, switching to bootstrapped.")
        bootstrapped = True


    if bootstrapped is True:
        if independent is True:
            result['N_resamples'] = N_resamples
            result['method'] = "A bootstrapped independent-samples t-test (n sim = %i) was conducted to compare %s by %s." %(result['N_resamples'], var1_name, var2_name)
        else:
            result['N_resamples'] = N_resamples
            result['method'] = "A bootstrapped pairwise t-test (n sim = %i) was conducted to compare %s and %s." %(result['N_resamples'], var1_name, var2_name)

        total_population = var1 + var2

        all_diffs = []
        for sample in range(N_resamples):
            np.random.shuffle(total_population)

            resampled1 = total_population[0:len(var1)]
            resampled2 = total_population[len(var2):]
            all_diffs.append(np.mean(resampled1) - np.mean(resampled2))

        percent = scipy.stats.percentileofscore(all_diffs,result['difference'])
        if percent > 50:
            p = (100-percent)/100
        else:
            p = percent/100
        result['p'] = p*2
        result['indices'] =  "Δ = %.2f, p = %.3f." %(result['difference'], result['p'])


    else:
        if independent is True:
            result['method'] = "A independent-samples t-test was conducted to compare %s by %s." %(var1_name, var2_name)
            result['t'], result['p'] = scipy.stats.ttest_ind(var1,var2)
        else:
            result['method'] = "A pairwise t-test was conducted to compare %s and %s." %(var1_name, var2_name)
            result['t'], result['p'] = scipy.stats.ttest_rel(var1,var2)
        result['indices'] =  "Δ = %.2f, t(%i) = %.3f, p = %.3f." %(result['difference'], result['dof'], result['t'], result['p'])






    if result['p'] < significance_treshold:
        is_significant = "a"
    else:
        is_significant = "no"

    if independent is True:
        result['interpretation'] = "There was %s significant difference of %s between the two groups of %s: %s (n = %i, M = %.2f, SD = %.2f) and %s (n = %i, M = %.2f, SD = %.2f);" %(is_significant, var1_name, var2_name, factor1, result['n1'], result['mean1'], result['sd1'], factor2, result['n2'], result['mean2'], result['sd2'])

    else:
        result['interpretation'] = "There was %s significant difference between VAR1 (n = %i, M = %.2f, SD = %.2f) and VAR2 (n = %i, M = %.2f, SD = %.2f);" %(is_significant, result['n1'], result['mean1'], result['sd1'], result['n1'], result['mean2'], result['sd2'])

    result['APA_output'] = "%s %s %s %s" %(result['method'], result['interpretation'], result['indices'], result['interpretation_d'])
    if output is True:
        print(result['APA_output'])
    return(result)











# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def bayesian_model(y, x, data=None, correlation=False, family="Normal", robust = True, samples = 1000, plot_posterior=True, plot_regression=True, plot_samples = "default", print_summary=True, alpha = 0.05):
    """
    Performs a Bayesian regression.

    Parameters
    ----------
    NA

    Returns
    ----------
    NA

    Example
    ----------
    NA

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - pandas
    - numpy
    - plotly
    - scipy
    - pymc3
    """

    print("Starting Bayesian estimation...")
    from theano import config
    config.warn.sum_div_dimshuffle_bug = False
    import pymc3



    y_name = "y"
    x_name = "x"

    if isinstance(y,str):
        y_name = y
        try:
            y = data[y]
        except:
            pass
    if isinstance(x,str):
        x_name = x
        try:
            x = data[x]
        except:
            pass


    if correlation == True:
        #Center and scale
        x = x - np.mean(x)
        x = x / np.std(x)

        y = y - np.mean(y)
        y = y / np.std(y)




    data = {y_name:y,
            x_name:x}
    formula = y_name + ' ~ ' + x_name










    with pymc3.Model() as model: # model specifications in PyMC3 are wrapped in a with-statement
        if family == "Normal":
            family = pymc3.glm.families.Normal()
            if robust == True:
                family = pymc3.glm.families.StudentT()

        pymc3.glm.glm(formula, data, family=family)
        start = pymc3.find_MAP()
        step = pymc3.NUTS(scaling=start) # Instantiate MCMC sampling algorithm
        trace = pymc3.sample(samples, step, progressbar=True) # draw 2000 posterior samples using NUTS sampling

#    trace = trace[int(samples/4):]
    #PLOT POSTERIOR DISTRIBUTION
    if plot_posterior == True:
        pymc3.traceplot(trace)

    #PLOT LINES
    if plot_regression == True:
        plot_data= []
        plot_data.append(go.Scatter(x=x,
                        y=y,
                        mode = 'markers'))



        if plot_samples == "default":
            if len(trace) > 100:
                plot_samples = 100
                samples_range = np.random.randint(0, len(trace), plot_samples)
            else:
                plot_samples = samples
                samples_range = range(len(trace))
        else:
            samples_range = np.random.randint(0, len(trace), plot_samples)



        for i in samples_range:
            print(i)
            plot_data.append(go.Scatter(x=x,
                            y=trace[i]['Intercept'] + trace[i]['x'] * x,
                            mode = 'lines',
                            opacity=0.25,
                            line = {"color":"grey",
                                    "width":5}))
        layout = go.Layout(showlegend=False)
        figure = go.Figure(data = plot_data,layout=layout)
        py.plot(figure)

    if print_summary == True:
        print(pymc3.summary(trace,alpha=alpha))
    return(trace)


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def dprime(n_Hit=None, n_Miss=None, n_FA=None, n_CR=None):
    """
    Calculates d', beta, c & ad'.

    see http://lindeloev.net/?p=29

    Parameters
    ----------
    NA

    Returns
    ----------
    NA

    Example
    ----------
    NA

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - scipy
    """
    Z = scipy.stats.norm.ppf
    # Floors an ceilings are replaced by half hits and half FA's
    half_Hit = 0.5/(n_Hit + n_Miss)
    half_FA = 0.5/(n_FA + n_CR)

    # Calculate hitrate and avoid d' infinity
    Hit_Rate = n_Hit/(n_Hit+n_Miss)
    if Hit_Rate == 1:
        Hit_Rate = 1-half_Hit
    if Hit_Rate == 0:
        Hit_Rate = half_Hit

    # Calculate false alarm rate and avoid d' infinity
    FA_Rate = n_FA/(n_FA+n_CR)
    if FA_Rate == 1:
        FA_Rate = 1-half_FA
    if FA_Rate == 0:
        FA_Rate = half_FA

    # Return d', beta, c and Ad'
    out = {}
    out['Hit_Rate'] = Hit_Rate
    out['FA_Rate'] = FA_Rate
    out['d'] = Z(Hit_Rate) - Z(FA_Rate)
    out['beta'] = math.exp(Z(FA_Rate)**2 - Z(Hit_Rate)**2)/2
    out['c'] = -(Z(Hit_Rate) + Z(FA_Rate))/2
    out['Ad'] = scipy.stats.norm.cdf(out['d']/math.sqrt(2))
    return(out)


# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def identify_outliers(serie, treshold=2.58):
    """
    Identify outliers.

    Parameters
    ----------
    serie = list or array
        data
    treshold = float
        maximum deviation (in terms of standart deviation). Following a gaussian distribution, 2.58 = rejecting 1%, 2.33 = rejecting 2%, 1.96 = 5% and 1.28 = rejecting 10%.

    Returns
    ----------
    NA

    Example
    ----------
    NA

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - scipy
    """
    outlier_list = []
    for i in serie:
        if abs(i - np.mean(serie))/np.std(serie) < treshold:
            outlier_list.append(0)
        else:
            outlier_list.append(1)
    serie_without_outliers = serie[abs(serie - np.mean(serie)) < treshold * np.std(serie)]
    return (outlier_list, serie_without_outliers)



# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
# ==============================================================================
def z_score(raw_score):
    """
    Transform an numeric pandas' array or list into Z scores (scaled and centered scores).

    Parameters
    ----------
    NA

    Returns
    ----------
    NA

    Example
    ----------
    NA

    Authors
    ----------
    Dominique Makowski

    Dependencies
    ----------
    - scipy
    """
    array = pd.Series(raw_score)

    mean = array.mean()
    sd = array.std(ddof=0)

    Z = (array-mean)/sd

    return(list(Z))