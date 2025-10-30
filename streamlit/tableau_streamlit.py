import streamlit as st
import streamlit.components.v1 as components

def main():
    st.markdown("# Visualizing WM's Men's Gymnastics")

    st.markdown("""
        This visualization is a dashboard created with Tableau to display the statistical performance of
                William and Mary's Division I Men's Gymnastics Team as a whole.
                """)
    
    html_temp = """
    <div class='tableauPlaceholder' id='viz1717198140682' style='position: relative'>
        <noscript>
            <a href='#'>
                <img alt='Team' src='https://public.tableau.com/static/images/Tr/TribeGymData/Team/1_rss.png' style='border: none' />
            </a>
        </noscript>
        <object class='tableauViz' style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
            <param name='embed_code_version' value='3' />
            <param name='site_root' value='' />
            <param name='name' value='TribeGymData/Team' />
            <param name='tabs' value='no' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https://public.tableau.com/static/images/Tr/TribeGymData/Team/1.png' />
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-US' />
        </object>
    </div>
    <script type='text/javascript'>
        var divElement = document.getElementById('viz1717198140682');
        var vizElement = divElement.getElementsByTagName('object')[0];
        if (divElement.offsetWidth > 800) {
            vizElement.style.minWidth = '420px';
            vizElement.style.maxWidth = '650px';
            vizElement.style.width = '100%';
            vizElement.style.minHeight = '587px';
            vizElement.style.maxHeight = '887px';
            vizElement.style.height = (divElement.offsetWidth * 0.80) + 'px';
        } else if (divElement.offsetWidth > 500) {
            vizElement.style.minWidth = '420px';
            vizElement.style.maxWidth = '650px';
            vizElement.style.width = '100%';
            vizElement.style.minHeight = '587px';
            vizElement.style.maxHeight = '887px';
            vizElement.style.height = (divElement.offsetWidth * 0.75) + 'px';
        } else {
            vizElement.style.width = '100%';
            vizElement.style.height = '1077px';
        }
        var scriptElement = document.createElement('script');
        scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
        vizElement.parentNode.insertBefore(scriptElement, vizElement);
    </script>
    """
    components.html(html_temp, height=900, width=1500)

    st.markdown("""
    ## Dashboard Description
    - Extracted data consists of all available individual scores from 2020 to the Eastern College Athletic Conference (ECAC) competition of 2024.
    - **Data Source:** Scores provided on William and Mary official website.
    - *Team score displays score potential rather than the exact score. That is the top 5 scores of event are used to determine the team score.*
    
    *This dashboard also includes a link to view the [**individual reports**](https://www.dropbox.com/scl/fo/qryou1360vokeo6gj3mi8/APZrZ5UkKwyJgHmR6Q2_wl4?rlkey=q6b6p8obrd28uu6qrflyliv74&e=1&st=409yhrpq&dl=0) generated for each athlete.*
    """)

if __name__ == "__main__":
    main()
