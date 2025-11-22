import marimo

__generated_with = "0.9.14"
app = marimo.App(width="medium")


@app.cell
def __():
    """
    Interactive Data Analysis Notebook
    Author: 23f2000060@ds.study.iitm.ac.in
    
    This notebook demonstrates reactive data analysis with Marimo.
    It explores the relationship between sample size and statistical confidence.
    """
    import marimo as mo
    import numpy as np
    import pandas as pd
    import plotly.express as px
    import plotly.graph_objects as go
    from scipy import stats
    
    mo.md("""
    # 📊 Interactive Statistical Analysis Dashboard
    
    **Author:** 23f2000060@ds.study.iitm.ac.in
    
    This notebook demonstrates the **Central Limit Theorem** and how sample size 
    affects the distribution of sample means. All cells are reactively connected - 
    changing any parameter will automatically update all dependent visualizations.
    """)
    return mo, np, pd, px, go, stats


@app.cell
def __(mo):
    """
    CELL 1: Interactive Controls
    
    This cell defines the interactive widgets that control the entire analysis.
    All subsequent cells depend on these parameters.
    
    Data Flow: This cell → generates parameters → used by data generation cell
    """
    
    mo.md("""
    ## 🎛️ Control Panel
    
    Adjust the parameters below to see how they affect the statistical distribution:
    """)
    
    # Interactive slider for sample size
    sample_size_slider = mo.ui.slider(
        start=10,
        stop=1000,
        step=10,
        value=100,
        label="Sample Size (n)",
        show_value=True
    )
    
    # Interactive slider for number of samples
    num_samples_slider = mo.ui.slider(
        start=100,
        stop=5000,
        step=100,
        value=1000,
        label="Number of Samples",
        show_value=True
    )
    
    # Interactive slider for population mean
    pop_mean_slider = mo.ui.slider(
        start=0,
        stop=100,
        step=5,
        value=50,
        label="Population Mean (μ)",
        show_value=True
    )
    
    # Interactive slider for population standard deviation
    pop_std_slider = mo.ui.slider(
        start=1,
        stop=30,
        step=1,
        value=15,
        label="Population Std Dev (σ)",
        show_value=True
    )
    
    # Display all controls
    mo.vstack([
        sample_size_slider,
        num_samples_slider,
        pop_mean_slider,
        pop_std_slider
    ])
    return (
        num_samples_slider,
        pop_mean_slider,
        pop_std_slider,
        sample_size_slider,
    )


@app.cell
def __(
    mo,
    num_samples_slider,
    pop_mean_slider,
    pop_std_slider,
    sample_size_slider,
):
    """
    CELL 2: Dynamic Parameter Display
    
    This cell reactively displays the current parameter values in a formatted way.
    It depends on all slider values from CELL 1.
    
    Data Flow: CELL 1 (sliders) → This cell → formatted output
    """
    
    # Extract values from sliders
    _sample_size = sample_size_slider.value
    _num_samples = num_samples_slider.value
    _pop_mean = pop_mean_slider.value
    _pop_std = pop_std_slider.value
    
    # Calculate theoretical standard error
    _theoretical_se = _pop_std / (_sample_size ** 0.5)
    
    # Dynamic markdown with emoji indicators based on sample size
    _size_indicator = "🔴" if _sample_size < 30 else "🟡" if _sample_size < 100 else "🟢"
    _confidence_level = "Low" if _sample_size < 30 else "Medium" if _sample_size < 100 else "High"
    
    mo.md(f"""
    ### 📋 Current Configuration
    
    {_size_indicator} **Sample Size:** {_sample_size} (Confidence: {_confidence_level})
    
    - **Number of Samples:** {_num_samples:,}
    - **Population Mean (μ):** {_pop_mean}
    - **Population Std Dev (σ):** {_pop_std}
    - **Theoretical Standard Error:** {_theoretical_se:.4f}
    
    {'⚠️ **Note:** Sample size < 30 may not show normal distribution clearly.' if _sample_size < 30 else ''}
    {'✅ **Good:** Sample size ≥ 100 provides excellent approximation to normal distribution.' if _sample_size >= 100 else ''}
    """)
    return


@app.cell
def __(
    _num_samples,
    _pop_mean,
    _pop_std,
    _sample_size,
    np,
    pd,
    stats,
):
    """
    CELL 3: Data Generation
    
    This cell generates synthetic data based on parameters from CELL 1.
    It creates multiple samples and calculates their means.
    
    Data Flow: CELL 1 (parameters) → This cell → raw data → CELL 4 (analysis)
    
    Dependencies:
    - sample_size_slider.value → _sample_size
    - num_samples_slider.value → _num_samples
    - pop_mean_slider.value → _pop_mean
    - pop_std_slider.value → _pop_std
    """
    
    # Set random seed for reproducibility
    np.random.seed(42)
    
    # Generate samples from normal distribution
    # Each row is one sample of size _sample_size
    samples = np.random.normal(
        loc=_pop_mean, 
        scale=_pop_std, 
        size=(_num_samples, _sample_size)
    )
    
    # Calculate mean of each sample (Central Limit Theorem in action!)
    sample_means = np.mean(samples, axis=1)
    
    # Calculate statistics
    observed_mean = np.mean(sample_means)
    observed_std = np.std(sample_means)
    theoretical_std = _pop_std / np.sqrt(_sample_size)
    
    # Create DataFrame for easier plotting
    df_samples = pd.DataFrame({
        'sample_mean': sample_means,
        'sample_id': range(_num_samples)
    })
    
    # Statistics summary
    stats_summary = {
        'Observed Mean': observed_mean,
        'Theoretical Mean': _pop_mean,
        'Observed Std Error': observed_std,
        'Theoretical Std Error': theoretical_std,
        'Mean Difference': abs(observed_mean - _pop_mean),
        'Std Error Difference': abs(observed_std - theoretical_std)
    }
    
    stats_df = pd.DataFrame([stats_summary]).T
    stats_df.columns = ['Value']
    return (
        df_samples,
        observed_mean,
        observed_std,
        sample_means,
        samples,
        stats_df,
        stats_summary,
        theoretical_std,
    )


@app.cell
def __(mo, stats_df):
    """
    CELL 4: Statistical Summary Display
    
    This cell displays the statistical summary table.
    It depends on the data generated in CELL 3.
    
    Data Flow: CELL 3 (generated data) → This cell → formatted table
    """
    
    mo.md(f"""
    ### 📈 Statistical Summary
    
    Comparison between observed and theoretical values:
    
    {mo.ui.table(stats_df, selection=None)}
    
    The closer the observed values are to theoretical values, 
    the better the Central Limit Theorem approximation.
    """)
    return


@app.cell
def __(
    _num_samples,
    _pop_mean,
    _pop_std,
    _sample_size,
    df_samples,
    go,
    observed_mean,
    observed_std,
    px,
    stats,
    theoretical_std,
):
    """
    CELL 5: Interactive Visualization
    
    This cell creates interactive plots showing the distribution of sample means.
    It depends on data from CELL 3 and parameters from CELL 1.
    
    Data Flow: 
    - CELL 1 (parameters) → CELL 3 (data) → This cell → visualizations
    """
    
    # Create histogram of sample means
    fig_hist = px.histogram(
        df_samples,
        x='sample_mean',
        nbins=50,
        title=f'Distribution of Sample Means (n={_sample_size}, samples={_num_samples})',
        labels={'sample_mean': 'Sample Mean', 'count': 'Frequency'},
        color_discrete_sequence=['#636EFA']
    )
    
    # Add normal distribution overlay
    x_range = np.linspace(
        df_samples['sample_mean'].min(),
        df_samples['sample_mean'].max(),
        100
    )
    
    # Theoretical normal distribution
    theoretical_pdf = stats.norm.pdf(
        x_range, 
        loc=_pop_mean, 
        scale=theoretical_std
    ) * len(df_samples) * (df_samples['sample_mean'].max() - df_samples['sample_mean'].min()) / 50
    
    fig_hist.add_trace(
        go.Scatter(
            x=x_range,
            y=theoretical_pdf,
            mode='lines',
            name='Theoretical Normal',
            line=dict(color='red', width=3, dash='dash')
        )
    )
    
    # Add vertical line for observed mean
    fig_hist.add_vline(
        x=observed_mean,
        line_dash="dot",
        line_color="green",
        annotation_text=f"Observed Mean: {observed_mean:.2f}",
        annotation_position="top"
    )
    
    fig_hist.update_layout(
        showlegend=True,
        height=500,
        hovermode='x unified'
    )
    
    # Create Q-Q plot to check normality
    fig_qq = go.Figure()
    
    # Calculate theoretical quantiles
    theoretical_quantiles = stats.norm.ppf(
        np.linspace(0.01, 0.99, len(sample_means)),
        loc=_pop_mean,
        scale=theoretical_std
    )
    
    observed_quantiles = np.sort(sample_means)
    
    fig_qq.add_trace(
        go.Scatter(
            x=theoretical_quantiles,
            y=observed_quantiles,
            mode='markers',
            name='Q-Q Plot',
            marker=dict(size=5, color='blue', opacity=0.6)
        )
    )
    
    # Add diagonal reference line
    min_val = min(theoretical_quantiles.min(), observed_quantiles.min())
    max_val = max(theoretical_quantiles.max(), observed_quantiles.max())
    
    fig_qq.add_trace(
        go.Scatter(
            x=[min_val, max_val],
            y=[min_val, max_val],
            mode='lines',
            name='Perfect Normal',
            line=dict(color='red', dash='dash', width=2)
        )
    )
    
    fig_qq.update_layout(
        title='Q-Q Plot: Sample Means vs Theoretical Normal',
        xaxis_title='Theoretical Quantiles',
        yaxis_title='Observed Quantiles',
        height=500,
        showlegend=True
    )
    
    # Display both plots
    visualization_output = [fig_hist, fig_qq]
    return (
        fig_hist,
        fig_qq,
        max_val,
        min_val,
        observed_quantiles,
        theoretical_pdf,
        theoretical_quantiles,
        visualization_output,
        x_range,
    )


@app.cell
def __(mo, visualization_output):
    """
    CELL 6: Display Visualizations
    
    This cell displays the interactive plots created in CELL 5.
    
    Data Flow: CELL 5 (plots) → This cell → rendered output
    """
    
    mo.md("""
    ### 📊 Interactive Visualizations
    
    **Histogram:** Shows the distribution of sample means. The red dashed line 
    represents the theoretical normal distribution predicted by the Central Limit Theorem.
    
    **Q-Q Plot:** Tests normality by comparing observed quantiles against theoretical 
    quantiles. Points should fall on the diagonal line if data is normally distributed.
    """)
    
    mo.vstack(visualization_output)
    return


@app.cell
def __(mo, observed_mean, observed_std, sample_size_slider, theoretical_std):
    """
    CELL 7: Dynamic Insights with Conditional Formatting
    
    This cell provides interpretation based on the current parameter values.
    It uses conditional logic to give different insights based on sample size.
    
    Data Flow: 
    - CELL 1 (sample_size) → This cell → conditional insights
    - CELL 3 (statistics) → This cell → interpretation
    """
    
    _current_sample_size = sample_size_slider.value
    _error_percentage = abs(observed_std - theoretical_std) / theoretical_std * 100
    
    # Generate different insights based on sample size
    if _current_sample_size < 30:
        _insight = f"""
        ### ⚠️ Small Sample Size Alert
        
        With **n = {_current_sample_size}**, the Central Limit Theorem approximation 
        may not be very accurate. Consider increasing the sample size to at least 30 
        for better results.
        
        **Current Error:** {_error_percentage:.2f}% difference between observed and theoretical std error.
        """
    elif _current_sample_size < 100:
        _insight = f"""
        ### 🟡 Moderate Sample Size
        
        With **n = {_current_sample_size}**, you're getting a decent approximation to 
        the normal distribution. The Central Limit Theorem is working!
        
        **Current Error:** {_error_percentage:.2f}% difference between observed and theoretical std error.
        
        **Tip:** Increase to n ≥ 100 for even better approximation.
        """
    else:
        _insight = f"""
        ### ✅ Excellent Sample Size!
        
        With **n = {_current_sample_size}**, the distribution of sample means closely 
        follows a normal distribution, exactly as predicted by the Central Limit Theorem!
        
        **Current Error:** {_error_percentage:.2f}% difference between observed and theoretical std error.
        
        - Observed Mean: **{observed_mean:.4f}**
        - Observed Std Error: **{observed_std:.4f}**
        - Theoretical Std Error: **{theoretical_std:.4f}**
        
        The small difference shows excellent agreement between theory and observation! 🎉
        """
    
    mo.md(_insight)
    return


@app.cell
def __(mo, sample_size_slider):
    """
    CELL 8: Visual Indicator Based on Sample Size
    
    This cell creates a dynamic visual indicator that changes based on sample size.
    It demonstrates reactive markdown with emojis.
    
    Data Flow: CELL 1 (sample_size_slider) → This cell → emoji indicator
    """
    
    _size = sample_size_slider.value
    _emoji_count = min(_size // 10, 50)  # Cap at 50 emojis for display
    
    if _size < 30:
        _emoji = "🔴"
        _status = "SMALL"
        _color = "#ff4444"
    elif _size < 100:
        _emoji = "🟡"
        _status = "MEDIUM"
        _color = "#ffaa00"
    else:
        _emoji = "🟢"
        _status = "LARGE"
        _color = "#44ff44"
    
    mo.md(f"""
    ### Sample Size Indicator
    
    <div style="background-color: {_color}22; padding: 20px; border-radius: 10px; border-left: 5px solid {_color};">
    
    **Status: {_status}**
    
    {_emoji * _emoji_count}
    
    **n = {_size}** (Each {_emoji} represents ~10 samples)
    
    </div>
    """)
    return


@app.cell
def __(mo):
    """
    CELL 9: Conclusion and Key Takeaways
    
    This is a static cell providing summary information about the notebook.
    """
    
    mo.md("""
    ---
    
    ## 🎓 Key Takeaways
    
    1. **Central Limit Theorem (CLT):** Regardless of the population distribution, 
       the distribution of sample means approaches a normal distribution as sample 
       size increases.
    
    2. **Sample Size Matters:** Larger samples (n ≥ 30-100) provide better 
       approximations to the theoretical normal distribution.
    
    3. **Standard Error:** The standard deviation of sample means decreases as 
       sample size increases, following the formula: SE = σ / √n
    
    4. **Practical Implications:** This is why larger sample sizes give more 
       reliable estimates in statistical inference.
    
    ---
    
    ### 📚 Further Resources
    
    - [Central Limit Theorem - Wikipedia](https://en.wikipedia.org/wiki/Central_limit_theorem)
    - [Marimo Documentation](https://docs.marimo.io)
    - [Statistical Inference - Khan Academy](https://www.khanacademy.org/math/statistics-probability)
    
    ---
    
    **Author:** 23f2000060@ds.study.iitm.ac.in  
    **Created with:** Marimo - Reactive Python Notebooks  
    **License:** MIT
    """)
    return


@app.cell
def __():
    """
    CELL 10: Environment Information
    
    This cell provides information about the notebook environment.
    Static cell with no dependencies.
    """
    import sys
    import platform
    
    env_info = f"""
    ## 💻 Environment Information
    
    - **Python Version:** {sys.version.split()[0]}
    - **Platform:** {platform.system()} {platform.release()}
    - **Marimo:** Reactive notebook environment
    
    This notebook demonstrates reactive programming where all cells 
    automatically update when dependencies change.
    """
    return env_info, platform, sys


@app.cell
def __(env_info, mo):
    mo.md(env_info)
    return


if __name__ == "__main__":
    app.run()
