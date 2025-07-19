from django.core.paginator import Paginator, Page
from django.http.request import HttpRequest
from typing import Any
from math import ceil
from recipes.models import Recipe


def make_pagination_range(
        page_range: range,
        pages: int,
        current_page: int,
) -> dict[str, Any]:
    middle_range: int = ceil(pages / 2)
    start_range: int = current_page - middle_range
    stop_range: int = current_page + middle_range
    total_pages: int = len(page_range)

    offset_range: int = abs(start_range) if start_range < 0 else 0

    if start_range < 0:
        start_range = 0
        stop_range += offset_range

    if stop_range >= total_pages:
        start_range = start_range - abs(total_pages - stop_range)

    pagination: list = page_range[start_range:stop_range]
    return {
        'pagination': pagination,
        'page_range': page_range,
        'pages': pages,
        'current_page': current_page,
        'total_pages': total_pages,
        'start_range': start_range,
        'stop_range': stop_range,
        'first_page_out_of_range': current_page > middle_range,
        'last_page_out_of_range': stop_range < total_pages
    }


def make_pagination(
        request: HttpRequest,
        queryset: Recipe,
        per_page: int,
        pages: int
        ) -> tuple[Page[Recipe], dict[str, Any]]:
    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1

    paginator = Paginator(queryset, per_page)
    page_obj = paginator.get_page(current_page)

    pagination_range = make_pagination_range(
        page_range=paginator.page_range,
        pages=pages,
        current_page=current_page
    )

    return page_obj, pagination_range, current_page
