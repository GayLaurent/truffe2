from django.db.models import Q
from django.shortcuts import render


def generic_list_json(request, model, columns, templates, bonus_data={}, check_deleted=False, filter_fields=[], bonus_filter_function=None, bonus_filter_function_with_parameters=None, deca_one_status=False, not_sortable_columns=[], selector_column=False, columns_mapping=None, bonus_total_filter_function=None):
    """Generic function for json list"""

    if not filter_fields:
        filter_fields = columns

    not_sortable_columns_local = not_sortable_columns + (model.MetaData.not_sortable_columns if hasattr(model, 'MetaData') and hasattr(model.MetaData, 'not_sortable_columns') else [])
    columns_mapping_local = model.MetaData.trans_sort if hasattr(model, 'MetaData') and hasattr(model.MetaData, 'trans_sort') else (columns_mapping or {})
    
    def request_get(key, default):
        if key in request.GET:
            return request.GET[key]
        elif key in request.POST:
            return request.POST[key]
        else:
            return default

    def do_ordering(qs):

        # Ordering
        try:
            i_sorting_cols = int(request_get('iSortingCols', 0))
        except:
            i_sorting_cols = 0

        order = []
        for i in range(i_sorting_cols):
            try:
                i_sort_col = int(request_get('iSortCol_%s' % i, 0))
            except ValueError:
                i_sort_col = 0
            s_sort_dir = request_get('sSortDir_%s' % i, '')

            sdir = '-' if s_sort_dir == 'desc' else ''

            sortcol = columns[i_sort_col + (-1 if selector_column else 0)]

            if isinstance(sortcol, list):
                for sc in sortcol:
                    if sc not in not_sortable_columns_local:
                        order.append('%s%s' % (sdir, columns_mapping_local.get(sc, sc)))
            else:
                if sortcol not in not_sortable_columns_local:
                    order.append('%s%s' % (sdir, columns_mapping_local.get(sortcol, sortcol)))

        if '-pk' not in order and 'pk' not in order:
            order.append('-pk')

        if order:
            qs = qs.order_by(*order)

        return qs

    def do_paging(qs):
        limit = min(int(request_get('iDisplayLength', 10)), 500)
        if limit == -1:
            return qs
        start = int(request_get('iDisplayStart', 0))
        offset = start + limit
        return qs[start:offset]

    def do_filtering(qs):
        sSearch = request_get('sSearch', None)

        if sSearch:

            general_base = None

            for subSearch in sSearch.split(' '):

                if subSearch:

                    base = Q(**{filter_fields[0] + '__icontains': subSearch})

                    for col in filter_fields[1:]:
                        base = base | Q(**{col + '__icontains': subSearch})

                    if not general_base:
                        general_base = base
                    else:
                        general_base = general_base & base

            if general_base:
                qs = qs.filter(general_base)

        if hasattr(model, 'MetaState') and hasattr(model.MetaState, 'status_col_id'):
            status_search = request_get('sSearch_%s' % (model.MetaState.status_col_id + (0 if not deca_one_status else 0) + (0 if selector_column else 0),), None)

            if status_search == "null":
                status_search = None

            if status_search:
                status_search_splited = status_search.split(',')

                base = Q(status=status_search_splited[0])

                for v in status_search_splited[1:]:
                    base = base | Q(status=v)

                qs = qs.filter(base)

        if bonus_filter_function:
            qs = bonus_filter_function(qs)

        if bonus_filter_function_with_parameters:
            qs = bonus_filter_function_with_parameters(qs, request)

        return qs

    qs = model.objects.all()

    if check_deleted:
        qs = qs.filter(deleted=False)

    total_records = qs.count() if not bonus_total_filter_function else bonus_total_filter_function(qs).count()

    qs = do_filtering(qs)

    total_display_records = qs.count()

    qs = do_ordering(qs)
    qs = do_paging(qs)

    data = {'iTotalRecords': total_records, 'iTotalDisplayRecords': total_display_records, 'sEcho': int(request_get('sEcho', 0)), 'list': qs.all()}
    data.update(bonus_data)

    rep = render(request, templates, data, content_type='application/json')

    return rep
