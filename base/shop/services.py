def get_discounted_price(course):
    if course.discount > 0:
        return course.price * (1 - (course.discount / 100))
    return course.price
