if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here

    df.drop(columns='Unnamed: 0',inplace=True)


    fact_table=df[['Restaurant_id','reviews','rating','food','service','value','atmosphere']].reset_index(drop=True)
    fact_table['id']=fact_table.index

    restaurant_dim=df[['name','address','City','Country','About','Latitude','Longitude']].reset_index(drop=True)
    restaurant_dim['Restaurant_dim_id']=restaurant_dim.index

    restaurant_price_dim=df[['Pricing','price_range','min_price','max_price','Average_price']].reset_index(drop=True)
    restaurant_price_dim['price_id']=restaurant_price_dim.index

    restaurant_cuisine=df[['cuisines','Dietry']].reset_index(drop=True)
    restaurant_cuisine['cuisine_id']=restaurant_cuisine.index

    restaurant_type=df[['Features']].reset_index(drop=True)
    restaurant_type['feature_id']=restaurant_type.index

    return {"fact_table":fact_table.to_dict(orient="dict"),
    "restaurant_dim":restaurant_dim.to_dict(orient="dict"),
    "restaurant_price_dim":restaurant_price_dim.to_dict(orient="dict"),
    "restaurant_cuisine":restaurant_cuisine.to_dict(orient="dict"),
    "restaurant_type":restaurant_type.to_dict(orient="dict")}


    # return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
