# todo:
# skala verschiebt sich und ist kacke
# Zeit sollte in Tagen sein:
    # generiere Zeiten zu richtigen Tagen
#



import plotly.express as px
import pandas as pd

def add_data(data, instance,  hospital_scores, cur_time):
    for ident, h in instance.hospitals.items():
        data.append([cur_time, ident, h.position.lat, h.position.lon, hospital_scores[ident]])

x_min = 5.7
x_max = 15.5
y_min = 47.2
y_max = 55

def hospital_visualization(instance, start, end, ticks):

    instance.snapshots = sorted(instance.snapshots, key = lambda s : s.filed_at)
    data_list = []

    hospital_scores = { ident : h.capacity_coefficient for ident, h in instance.hospitals.items()}

    i = 0
    for t in range(ticks):

        cur_time = round(start + t / ticks * (end - start))

        while i + 1 < len(instance.snapshots) and instance.snapshots[i + 1].filed_at <= cur_time:
            s = instance.snapshots[i]
            hospital_scores[s.hospital_ident] = s.capacity_coefficient
            i += 1

        add_data(data_list, instance, hospital_scores, cur_time)

    df = pd.DataFrame(data_list, columns = ['time', 'id', 'y', 'x', 'capacity_score'])

    fig = px.scatter(df, x = 'x', y = 'y', animation_frame= 'time', animation_group = 'id', color = 'capacity_score', color_continuous_scale=[(0.00, "green"),   (0.33, "yellow"),
                                                     (0.66, "red"), (1.0, "black")], hover_name = 'id', range_x = [x_min, x_max], range_y = [y_min, y_max], width=800, height=1200)
    fig.add_layout_image(dict(source="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Karte_Deutschland.svg/1000px-Karte_Deutschland.svg.png"),
            xref="x",
            yref="y",
            x = x_min,
            y = y_max,
            sizex = (x_max - x_min),
            sizey = (y_max - y_min),
            sizing="stretch",
            opacity=0.5,
            layer="below")
    fig.update_traces(marker=dict(size = 10))
    for frame in fig.frames:
        for i in range(len(frame.data)):
            frame.data[i]['marker']['symbol'] = 'square'

    #fig.show()

    html_dump = fig.to_html()
    with open("data/visualization/hospitals.html", "w") as f:
        f.write(html_dump)

def corona_visualization(instance, start, end, ticks):

    # visible for more time steps
    nbr_ticks_visible = 10

    reqs = sorted(instance.requests.values(), key = lambda r : r.filed_at)

    data_list = []
    times = [round(start + t / ticks * (end - start)) for t in range(ticks)]

    r_id = 0
    for t in range(ticks):

        cur_time = times[t]

        while r_id + 1 < len(reqs) and reqs[r_id + 1].filed_at <= cur_time:
            r = instance.requests[str(r_id)]
            for i in range(nbr_ticks_visible):
                if i + t >= ticks:
                    break
                data_list.append([times[i + t], r.ident, r.person.position.lon, r.person.position.lat])
            r_id += 1
    df = pd.DataFrame(data_list, columns = ['time', 'id', 'x', 'y'])


    fig = px.scatter(df, x = 'x', y = 'y', animation_frame= 'time', animation_group = 'id', hover_name = 'id', range_x = [x_min, x_max], range_y = [y_min, y_max], width=800, height=1200)
    fig.add_layout_image(dict(source="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e3/Karte_Deutschland.svg/1000px-Karte_Deutschland.svg.png"),
            xref="x",
            yref="y",
            x = x_min,
            y = y_max,
            sizex = (x_max - x_min),
            sizey = (y_max - y_min),
            sizing="stretch",
            opacity=0.5,
            layer="below")
    #fig.show()
    html_dump = fig.to_html()
    with open("data/visualization/patients.html", "w") as f:
        f.write(html_dump)


def visualize(instance, snapshots):
    instance.snapshots = snapshots
    time_frame_start = min(r.filed_at for r in instance.requests.values())
    time_frame_end = max(r.filed_at for r in instance.requests.values())
    nbr_ticks = 100

    hospital_visualization(instance, time_frame_start, time_frame_end, nbr_ticks)
    corona_visualization(instance, time_frame_start, time_frame_end, nbr_ticks)
