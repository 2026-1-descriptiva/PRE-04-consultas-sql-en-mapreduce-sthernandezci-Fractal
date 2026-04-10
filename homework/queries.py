"""Taller evaluable"""

# pylint: disable=broad-exception-raised
# pylint: disable=import-error

# import mapreduce.hadoop as run_mapreduce_job  # type: ignore
from homework.mapreduce import hadoop as run_mapreduce_job  # type: ignore

#
# Columns:
# total_bill, tip, sex, smoker, day, time, size
#


#
# SELECT *, tip/total_bill as tip_rate
# FROM tips;
#
def mapper_query_1(sequence):
    """Mapper"""
    result = []
    for index, (_, row) in enumerate(sequence):
        if index == 0:
            result.append((index, row.strip() + ",tip_rate"))
        else:
            row_values = row.strip().split(",")
            total_bill = float(row_values[0])
            tip = float(row_values[1])
            tip_rate = tip / total_bill
            result.append((index, row.strip() + "," + str(tip_rate)))
    return result


def reducer_query_1(sequence):
    """Reducer"""
    return sequence

#
# ORQUESTADOR:
#
def run():
    """Orquestador"""

    run_mapreduce_job(
        mapper_fn=mapper_query_1,
        reducer_fn=reducer_query_1,
        input_folder="files/input",
        output_folder="files/query_1",
    )

if __name__ == "__main__":

    run()