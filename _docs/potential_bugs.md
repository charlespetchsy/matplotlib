Segmentation Fault with Tricontour
https://github.com/matplotlib/matplotlib/issues/10167

Description:
Given an array of data where its lower or upper triangular values are populated with NaNs, tricontour and tricontourf is unable to draw contour lines and results in a segmentation fault, which further prevents the plot from being displayed.
